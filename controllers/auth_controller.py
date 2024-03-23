from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from psycopg2 import errorcodes

from init import db, bcrypt
from models.users import Users, user_schema

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def auth_register():
    try:
        # the data we get in body of request
        body_data = request.get_json()

        # create the user instance
        user = Users(
            name=body_data.get("name"),
            username=body_data.get("username"),
        )

        # password from the request body
        password = body_data.get("password")
        # before hashing, if password exists as non empty str, hash pw
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")

        # add and commit the user to db
        db.session.add(user)
        db.session.commit()
        # respond back to the client
        return user_schema.dump(user), 201
    # give integrityerror a name (err) to access what is inside it
    except IntegrityError as err:
        # print the postgresql integrity error code
        print(err.orig.pgcode)
        # import errorcodes from psycopg2 so we don't need to remember number codes
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            pass
            # use the column name to give a more dynamic error details
            return {"error": f"the {err.orig.diag.column_name} is required"}
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            pass
            # handle exception
            return {"error": "username already in use"}, 409

@auth_bp.route("/login", methods=["POST"])
def auth_login():
    body_data = request.get_json()
    # find user with username
    stmt = db.select(Users).filter_by(username=body_data.get("username"))
    # convert this to scalar value
    user = db.session.scalar(stmt)
    # if user exist and pw correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # create jwt
        token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=14))
        # return token with user info
        return {"username": user.username, "token": token, "is_admin": user.is_admin}
    else:
        return {"error": "invalid username or password"}, 401