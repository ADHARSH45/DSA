class Product:
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
    def __str__(self):
        return f"{self.name:<8} : {self.quantity:>8}"
    def change_quantity(self,new_quantity):
        self.quantity = new_quantity

class ShoppingList:
    def __init__(self,title):
        self.title = title
        self.items = []

    def __str__(self):
        return f"{self.title} has {len(self.items)} items"
    
    def add(self,product):
        if isinstance(product,Product):
            self.items.append(product)
            print("Item addedd sccessfully")
        else:
            print("Item need to be product")
    
    def show(self):
        print("Current Items")
        for item in self.items:
            print(f"{item.name:<12} : {item.quantity:>12}")
    