'''
시작 시각 :
종료 시각 :
'''


class Cake:
    def __init__(self):  sdaffsdafasd
        pass


class Shop:
    def __init__(self):
        pass

    def buy_ingredient(self, buy_dict):
        pass

    def current_ingredient(self):
        pass

    def make_cake(self, cake):
        pass


class Pos:
    def __init__(self):
        pass

    def current_cakes(self):
        pass

    def sell_cake(self, cakename):
        pass

    def print_current_money(self):
        pass


cheesecake = Cake("Cheese Cake", 6900, {'cheese': 2, 'egg': 2, 'butter': 2})
chococake = Cake("Chocolate Cake", 5900, {'chocolate': 2, 'egg': 2, 'butter': 2})
carrotcake = Cake("Carrot Cake", 5500, {'carrot': 2, 'walnut': 2, 'egg': 1, 'butter': 1})
creamcake = Cake("Fresh Cream Cake", 4500, {'cream': 3, 'egg': 1, 'butter': 1})
swpotatocake = Cake("Sweet Potato Cake", 6500, {'sweet potato': 3, 'egg': 2, 'butter': 1})

cake_shop = Shop()
cake_shop.buy_ingredient({'cheese': 5, 'carrot': 3, 'sweet potato': 3, 'egg': 10, 'butter': 10})
cake_shop.current_ingredient()
cake_shop.buy_ingredient({'chocolate': 3, 'walnut': 2, 'egg': 12, 'butter': 12})
cake_shop.current_ingredient()

print("\nMAKE CAKE")
cake_shop.make_cake(creamcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(carrotcake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(cheesecake)
print(cake_shop.ingredient)
cake_shop.make_cake(chococake)
print(cake_shop.ingredient)
cake_shop.make_cake(swpotatocake)
print(cake_shop.ingredient)
cake_shop.current_ingredient()

pos = Pos(cake_shop)
print()
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')
pos.current_cakes()

print()
pos.sell_cake('Chocolate Cake')
pos.current_cakes()

print()
pos.sell_cake('Cheese Cake')

print()
pos.print_current_money()
