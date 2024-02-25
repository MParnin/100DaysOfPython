import os
os.system("cls" if os.name == "nt" else "clear")

from day016_menu import Menu, MenuItem
from day016_coffee_maker import CoffeeMaker
from day016_money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
powered = True
while powered:
    options = menu.get_items()
    selection = input(f"What would you like? ({options}): ")
    if selection == "off":
        powered = False
    elif selection == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(selection)
    if coffee_maker.is_resource_sufficient(order):
        if money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)