from typing import List
from project.drink import Drink
from project.food import Food


class ProductRepository:

    def __init__(self):
        self.products: List[Food or Drink] = []

    def add(self, product: Food or Drink) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Food or Drink:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join(f"{product.name}: {product.quantity}" for product in self.products)
