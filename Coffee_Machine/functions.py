import menu
import resources


def coffee_cost():
    print(f"Espresso: ${menu.MENU['espresso']['cost']}")
    print(f"Latte: ${menu.MENU['latte']['cost']}")
    print(f"Cappuccino: ${menu.MENU['cappuccino']['cost']}")


def current_report():
    print(f"Water: {resources.resources['water']}ml")
    print(f"Milk: {resources.resources['milk']}ml")
    print(f"Coffee: {resources.resources['coffee']}g")
    print(f"Money: ${resources.resources['money']}")


def management(def_string):

    if def_string == 'cost':
        coffee_cost()

    elif def_string == 'report':
        current_report()


def money():

    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    def_money = (quarters * 0.25) + (dimes * .010) + (nickles * .05) + (pennies * 0.1)

    return def_money


def upgrade_resources(def_coffee):

    if def_coffee == 'espresso':
        resources.resources['water'] = resources.resources['water'] - menu.MENU['espresso']['ingredients']['water']
        resources.resources['coffee'] = resources.resources['coffee'] - menu.MENU['espresso']['ingredients']['coffee']
        resources.resources['money'] = resources.resources['money'] + menu.MENU['espresso']['cost']

        return resources.resources

    elif def_coffee == 'latte':
        resources.resources['water'] = resources.resources['water'] - menu.MENU['latte']['ingredients']['water']
        resources.resources['milk'] = resources.resources['milk'] - menu.MENU['latte']['ingredients']['milk']
        resources.resources['coffee'] = resources.resources['coffee'] - menu.MENU['latte']['ingredients']['coffee']
        resources.resources['money'] = resources.resources['money'] + menu.MENU['latte']['cost']

        return resources.resources

    elif def_coffee == 'cappuccino':
        resources.resources['water'] = resources.resources['water'] - menu.MENU['cappuccino']['ingredients']['water']
        resources.resources['milk'] = resources.resources['milk'] - menu.MENU['cappuccino']['ingredients']['milk']
        resources.resources['coffee'] = resources.resources['coffee'] - menu.MENU['cappuccino']['ingredients']['coffee']
        resources.resources['money'] = resources.resources['money'] + menu.MENU['cappuccino']['cost']

        return resources.resources


def receipt_espresso(def_money, def_coffee):

    if def_money < def_coffee:
        print(f"Too small an amount: ${round(def_money, 2)}")
        print(f"Coffee cost: ${def_coffee}")

    elif def_money > def_coffee:

        rest = round(def_money - def_coffee, 2)

        print(f"Here is your ${rest} in change.")
        print("Here is your espresso. Enjoy!")

    elif def_money == def_coffee:
        print("No rest")
        print("Here is your espresso. Enjoy!")


def receipt_latte(def_money, def_coffee):

    if def_money < def_coffee:
        print(f"Too small an amount: ${round(def_money, 2)}")
        print(f"Coffee cost: ${def_coffee}")

    elif def_money > def_coffee:

        rest = round(def_money - def_coffee, 2)

        print(f"Here is your ${rest} in change.")
        print("Here is your latte. Enjoy!")

    elif def_money == def_coffee:
        print("No rest")
        print("Here is your latte. Enjoy!")


def receipt_cappuccino(def_money, def_coffee):

    if def_money < def_coffee:
        print(f"Too small an amount: ${round(def_money, 2)}")
        print(f"Coffee cost: ${def_coffee}")

    elif def_money > def_coffee:

        rest = round(def_money - def_coffee, 2)

        print(f"Here is your ${rest} in change.")
        print("Here is your cappuccino. Enjoy!")

    elif def_money == def_coffee:
        print("No rest")
        print("Here is your cappuccino. Enjoy!")


def payment(def_payment):

    if def_payment == 'espresso':

        def_money = money()
        espresso = menu.MENU['espresso']['cost']

        receipt_espresso(def_money, espresso)

        upgrade_resources(def_payment)

    elif def_payment == 'latte':

        def_money = money()
        latte = menu.MENU['latte']['cost']

        receipt_latte(def_money, latte)

    elif def_payment == 'cappuccino':

        def_money = money()
        cappuccino = menu.MENU['cappuccino']['cost']

        receipt_cappuccino(def_money, cappuccino)


def check(def_coffee):
    if def_coffee == 'espresso':
        if resources.resources['water'] < menu.MENU['espresso']['ingredients']['water'] or resources.resources['coffee'] < menu.MENU['espresso']['ingredients']['coffee']:
            return False
        else:
            return True

    elif def_coffee == 'latte':
        if resources.resources['water'] < menu.MENU['latte']['ingredients']['water'] or resources.resources['milk'] < menu.MENU['latte']['ingredients']['milk'] or resources.resources['coffee'] < menu.MENU['latte']['ingredients']['coffee']:
            return False
        else:
            return True

    elif def_coffee == 'cappuccino':
        if resources.resources['water'] < menu.MENU['cappuccino']['ingredients']['water'] or resources.resources['milk'] < menu.MENU['cappuccino']['ingredients']['milk'] or resources.resources['coffee'] < menu.MENU['cappuccino']['ingredients']['coffee']:
            return False
        else:
            return True


def order(def_order):

    if def_order == 'espresso':
        if not check(def_order):
            print("Resources level too low")
        else:
            payment(def_order)

    elif def_order == 'latte':
        if not check(def_order):
            print("Resources level too low")
        else:
            payment(def_order)

    elif def_order == 'cappuccino':
        if not check(def_order):
            print("Resources level too low")
        else:
            payment(def_order)


def on_off_switch(def_choice):

    if def_choice == 'OFF':
        return False

    elif def_choice == 'ON':
        return True


def add_resources():
    print("Add resources: ")

    water = float(input("How much water: "))
    milk = float(input("How much milk: "))
    coffee = float(input("How much coffee: "))

    resources.resources['water'] = resources.resources['water'] + water
    resources.resources['milk'] = resources.resources['milk'] + milk
    resources.resources['coffee'] = resources.resources['coffee'] + coffee


def withdraw(def_money):

    if def_money > resources.resources['money']:

        print("Too much money you want to withdraw")

    elif def_money < resources.resources['money']:
        print("Withdraw money")
        resources.resources['money'] = resources.resources['money'] - def_money

        return resources.resources['money']

    elif def_money == resources.resources['money']:

        print("you cannot leave the treasury empty")
