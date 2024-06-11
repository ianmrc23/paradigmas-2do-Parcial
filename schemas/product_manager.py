from typing import List


class Product:
    def __init__(
        self,
        product_id: int,
        product_name: str,
        product_price: float,
        product_quantity: int,
        product_weight: float
    ):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.product_weight = product_weight


class Category:
    def __init__(
        self,
        category_id: int,
        category_name: str
    ):
        self.category_id = category_id
        self.category_name = category_name
        self.products: List[Product] = []
