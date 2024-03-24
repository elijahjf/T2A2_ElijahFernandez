from init import db, ma
from .florists import Florists

# create our own model by making a class that exdends from the SQLAlchemy model class.
class Users(db.Model):
    # create table name
    __tablename__ = "users"

    # now we write the structure of the table. We make each column and the different criteria for them
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    # relationship
    florist_profile = db.relationship("Florists", back_populates="user")

class UsersSchema(ma.Schema):
    # define fields we want to deserialise
    class Meta:
        fields = ("id", "name", "username", "password")

# to deserialise single user as a dict {}
user_schema = UsersSchema(exclude=["password"])
# to deserialise many users as a list of dict [{}, {}, {}]
users_schema = UsersSchema(many=True, exclude=["password"])
