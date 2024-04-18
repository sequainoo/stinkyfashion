"""Models a customer order"""
from models.base import Base


class Order(Base):
    customer_name = ""
    customer_phone = ""
    product_id = ""

