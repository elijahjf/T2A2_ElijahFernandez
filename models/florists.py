from init import db, ma

class Florists(db.Model):
    __tablename__ = "florists"

    florist_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    # role junior_florist or senior_florist
    role = db.Column(db.String, default="junior_florist")

    # add relationship back to the User
    user = db.relationship("Users")
    
class FloristsSchema(ma.Schema):
    # fields to deserialise
    class Meta:
        fields = ("florist_id", "user_id", "role")