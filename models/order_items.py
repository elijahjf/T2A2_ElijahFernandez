from init import db, ma

class OrderItems(db.Model):
    __tablename__ = "order_items"

    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db,ForeignKey("orders.order_id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    quantity = db.Column(db.Integer, default=1)

    # relationships
    order = db.relationship("Orders", back_populates="order_items")
    product = db.relationship("Products", back_populates="order_items")

class OrderItemsSchema(ma.Schema):
    class Meta:
        fields = ("order_item_id", "order_id", "product_id", "quantity")