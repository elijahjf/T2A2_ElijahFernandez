from init import db, ma
from sqlalchemy import Enum

# create our own model by making a class that exdends from the SQLAlchemy model class.
class Florists(db.Model):
    # create table name
    __tablename__ = "florists"

    florist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    # florist_role = db.Column(Enum("junior_florist", "senior_florist", name="florist_role_enum"), nullable=False, default=junior_florist)
    is_senior = db.Column(db.Boolean, default=False)

class FloristsSchema(ma.Schema):
    # fields to deserialise
    class Meta:
        fields = ("florist_id", "name", "username", "password", "is_senior")

from init import db, ma

# to deserialise single florist as a dict {}
florist_schema = FloristsSchema(exclude=["password"])
# to deserialise many florists as a list of dict [{}, {}, {}]
florists_schema = FloristsSchema(many=True, exclude=["password"])