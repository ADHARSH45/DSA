from shopping_list import ShoppingList,Product

p1 = Product("tomato",6)
p2 = Product("color pen",5)
p3 = Product("pencil",3)
p4 = Product("rice",10)
p5 = Product("potato",7)
p6 = Product("onion",9)

slist = ShoppingList("shoppingList")
slist.add(p1)
slist.add(p2)
slist.add(p3)
slist.add(p4)
slist.add(p5)
slist.add(p6)

slist.show()
