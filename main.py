from Inventory import Inventory
from Product import Product

inventory = Inventory()

pen = Product("Pen",20)
eraser = Product("Eraser", 50)

inventory.add_product(pen, 500)
inventory.add_product(eraser, 200)
inventory.remove_product(pen, 50)
inventory.remove_product(eraser, 250)

inventory.print_inventory()
