from init import db, ma
from sqlalchemy import Numeric

class Products(db.Model):
    __tablename__ = "products"

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    price = db.Column(Numeric(precision=10, scale=2))
    main_color = db.Column(db.String)
    flower_type = db.Column(db.String, choices=("native", "non_native"))

class ProductsSchema(ma.Schema):
    class Meta:
        fields = ("product_id", "product_name", "price", "main_color", "flower_type")