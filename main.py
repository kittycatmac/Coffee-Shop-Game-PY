from utilities import *
from coffee_shop_simulator import CoffeeShopSimulator

# print welcome page
welcome()

# get name and shop name
t_name = prompt("What is your name?", True)
t_shop_name = prompt("What do you want to nane your coffee shop?", True)

# create the game object
game = CoffeeShopSimulator(t_name, t_shop_name)

game.run()