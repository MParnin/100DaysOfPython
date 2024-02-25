process_order = False
resource_avail = False

menu = [
    {
        'name': 'espresso',
        'water': '50',
        'milk': '0',
        'coffee': '18',
        'cost': 1.5
    },
    {
        'name': 'latte',
        'water': '200',
        'milk': '150',
        'coffee': '24',
        'cost': 2.5
    },
    {
        'name': 'cappuccino',
        'water': '250',
        'milk': '100',
        'coffee': '24',
        'cost': 3.0
    },
]

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
    }

def check_resources(drink):
    global resource_avail
    needed_water = int(drink['water'])
    needed_milk = int(drink['milk'])
    needed_coffee = int(drink['coffee'])
    avail_water = resources['water'] - needed_water
    avail_milk = resources['milk'] - needed_milk
    avail_coffee = resources['coffee'] - needed_coffee
    if avail_water < 0:
        print("Sorry, there is not enough water.")
        return
    elif avail_milk < 0:
        print("Sorry, there is not enough milk.")
        return
    elif avail_coffee < 0:
        print("Sorry, there is not enough coffee.")
        return
    else:
        resource_avail = True
        return

def transaction(order):
    global process_order
    print("Please insert coins.")
    qty_quarters = int(input("How many quarters?: "))
    qty_dimes = int(input("How many dimes?: "))
    qty_nickels = int(input("How many nickels?: "))
    qty_pennies = int(input("How many pennies?: "))

    user_total = qty_quarters * 0.25 + qty_dimes * 0.1 + qty_nickels * 0.05 + qty_pennies * 0.01

    if user_total == order['cost']:
        process_order = True
        return

    elif user_total > order['cost']:
        user_change = round(user_total - order['cost'], 2)
        print(f"Here is ${user_change} in change.")
        process_order = True
        return

    elif user_total < order['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        return

def brew(order):
    global resources
    resources['water'] -= int(order['water'])
    resources['milk'] -= int(order['milk'])
    resources['coffee'] -= int(order['coffee'])
    resources['money'] += int(order['cost'])
    print(f"Here is your {order['name']}.  Enjoy!")
    return

def operate():
    global process_order
    global resource_avail
    powered = True
    while powered == True:
        process_order = False
        resource_avail = False
        selection = input("What would you like? (espresso/latte/cappuccino): ")
        if selection == 'off':
            powered = False
        elif selection == 'report':
            print(resources)
        elif selection == 'espresso' or 'latte' or 'cappuccino':
            for item in menu:
                if item['name'] == selection:
                    order = item
                    break
            else:
                order = None
            check_resources(order)
            if resource_avail == True:
                transaction(order)
            if process_order == True:
                brew(order)

operate()