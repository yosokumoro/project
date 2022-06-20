MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

#TODO 2 Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

coffee_machine_off = False

#TODO 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.




while coffee_machine_off == False:
    resources_water = resources["water"]
    resources_milk = resources["milk"]
    resources_coffee = resources["coffee"]
    resources_money = resources["money"]
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "OFF":
        coffee_machine_off = True
        print("Coffee machine off. Goodbye!")
#TODO 3 Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
    while choice == "report":
        print(f"the current resource values \nWater: {resources_water}ml\nMilk: {resources_milk}ml")
        print(f"Coffee: {resources_coffee}g\nMoney: ${resources_money}")
        choice = input("What would you like? (espresso/latte/cappuccino): ")
#todo 4 Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
    if choice == "espresso":
        if MENU[choice]["ingredients"]["water"] > resources_water:
            print("Sorry there is not enough water")
            coffee_machine_off = True
        if MENU[choice]["ingredients"]["coffee"] > resources_coffee:
            print("Sorry there is not enough water")
            coffee_machine_off = True
    elif choice == "latte" or choice == "cappuccino":
        if MENU[choice]["ingredients"]["water"] > resources_water:
            print("Sorry there is not enough water")
            coffee_machine_off = True
        if MENU[choice]["ingredients"]["milk"] > resources_milk:
            print("Sorry there is not enough milk")
            coffee_machine_off = True
        if MENU[choice]["ingredients"]["coffee"] > resources_coffee:
            print("Sorry there is not enough coffee")
            coffee_machine_off = True
    if coffee_machine_off != True:
        print ("Please insert coins.")
        quarter = float(input("how many quarters?: "))
        dime = float(input("how many dimes?: "))
        nickels = float(input("how many nickles?: "))
        pennies = float(input("how many pennies?: "))
        money = quarter*0.25+dime*0.1+nickels*0.05+pennies*0.01
        if money < MENU[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded")
        else:
            change = round(money - MENU[choice]["cost"],2)
            print(f"Here is your change {change}")
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["milk"] -=  MENU[choice]["ingredients"]["milk"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            resources["money"] += MENU[choice]["cost"]
            resources_water = resources["water"]
            resources_milk = resources["milk"]
            resources_coffee = resources["coffee"]
            resources_money = resources["money"]
            print(f"the current resource values \nWater: {resources_water}ml\nMilk: {resources_milk}ml")
            print(f"Coffee: {resources_coffee}g\nMoney: ${resources_money}")
            print(f"Here is your {choice}, enjoy!")
    elif choice != "OFF":
        coffee_machine_off = False

