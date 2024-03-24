from init import db, ma
from datetime import datetime
from sqlalchemy import Enum

class Orders(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"))
    florist_id = db.Column(db.Integer, db.ForeignKey("florists.florist_id"))
    date_ordered = db.Column(db.DateTime, default=datetime.now)
    pick_up_date = db.Column(db.DateTime)
    description = db.Column(db.String)
    order_status = db.Column(Enum("pending", "confirmed", "cancelled", "completed" "received"), name="order_status_enum")

class ProductsSchema(ma.Schema):
    class Meta:
        fields = ("product_id", "product_name", "price", "main_color", "flower_type")