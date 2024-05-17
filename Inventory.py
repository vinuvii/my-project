class Inventory:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products

    def add_product(self, product, quantity):
        if product.name in self._products:
            self._products[product.name]['quantity'] += quantity
        else:
            self._products[product.name] = {'product': product, 'quantity': quantity}

