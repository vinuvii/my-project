from Inventory import Inventory
from Product import Product

inventory = Inventory()

pen = Product("Pen",20)
eraser = Product("Eraser", 50)

inventory.add_product(pen, 500)
inventory.add_product(eraser, 200)


inventory.print_inventory()