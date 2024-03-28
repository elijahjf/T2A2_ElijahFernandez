from init import db, ma
from datetime import datetime
from sqlalchemy import Numeric, Enum

class Orders(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"))
    florist_id = db.Column(db.Integer, db.ForeignKey("florists.florist_id"))
    date_ordered = db.Column(db.DateTime, default=datetime.now)
    pick_up_date = db.Column(db.DateTime)
    description = db.Column(db.String)
    order_status = db.Column(Enum("pending", "confirmed", "cancelled", "completed" "received"), name="order_status_enum", default="pending")
    total_price = db.Column(Numeric(precision=10, scale=2))

    # relationships
    order_items = db.relationship("OrderItems", back_populates="order", lazy=dynamic)

class OrdersSchema(ma.Schema):
    class Meta:
        fields = ("order_id", "customer_id", "florist_id", "date_ordered", "pick_up_date", "description", "order_status")