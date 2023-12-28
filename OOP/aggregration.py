# Relationships between classes: association, aggregation, and composition
# Aggregation is a more specialized form of association
# between two or more objects. Each object will have
# its independent lifecycle.
# It's usually a one-to-many relationship, where one
# object has one or many objects.
# The objects can live separately, but it may be
# a relationship where one object needs another
# to perform a certain task.
# (there are controversies about the definitions of aggregation).
class ShoppingCart:
    def __init__(self) -> None:
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])
    
    def insert_products(self, *products):
        # self._products.extend(products) 
        self._products += products
    
    def list_products(self):
        for product in self._products:
            print(product.name, product.price)
            
class Product: 
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

shopping_cart = ShoppingCart()
product_one, product_two = Product('Pen', 1.20), Product('Shirt', 20)

shopping_cart.insert_products(product_one, product_two)
shopping_cart.list_products()
print(shopping_cart.total())