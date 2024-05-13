import functions

flag = True

print("""
1. 'espresso' - order espresso
2. 'latte' - order latte
3. 'cappuccino' - order cappuccino
4. 'report' - check of resources
5. 'cost' - current price of coffees
6. 'add' - for the service technician who completes resources
7. 'withdraw' - withdrawal of money
7. 'ON' - switching ON the machine
8. 'OFF' - switching OFF the machine
""")

while True:

    while flag:

        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            functions.order(choice)

        elif choice == 'report':
            functions.management(choice)

        elif choice == 'cost':
            functions.management(choice)

        elif choice == 'add':
            functions.add_resources()

        elif choice == 'withdraw':

            money = float(input("How much money do you want withdraw: "))

            functions.withdraw(money)

        elif choice == 'off':
            flag = functions.on_off_switch(choice.upper())

    on_off_switch = input("ON/ OFF ").upper()

    flag = functions.on_off_switch(on_off_switch)
