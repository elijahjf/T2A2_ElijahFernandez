from init import db, ma

class Customers(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String)
    customer_contact_number = db.Column(db.String)

    # relationships
    orders = db.relationship("Orders", back_populates="customers")

class CustomersSchema(ma.Schema):
    class Meta:
        fields = ("customer_id", "customer_name", "customer_contact_number")