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
            "water": 200,
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
    "money": 0.00
}

debug = False  # turn on/off debug statements
validItem = True
drink_paid = False


def check_resources():
    # if resources["water"] < MENU[coffeeType]["ingredients"]["water"]:
    #     print("There is not enough water.")
    #     return False
    # elif resources["milk"] < MENU[coffeeType]["ingredients"]["milk"]:  # error if choosing espresso
    #     print("There is not enough milk.")
    #     return False
    # elif resources["coffee"] < MENU[coffeeType]["ingredients"]["coffee"]:
    #     print("There is not enough coffee.")
    #     return False
    # else:
    #     return True

    for x in MENU[coffeeType]["ingredients"]:
        if resources[x] < MENU[coffeeType]["ingredients"][x]:
            print(f"There is not enough {x}.")
            return False

    return True


def process_coins():
    print("Please insert coins.")
    num_quarters = int(input("how many quarters?: "))
    num_dimes = int(input("how many dimes?: "))
    num_pennies = int(input("how many pennies?: "))

    paid_amt = round(((num_quarters * .25) + (num_dimes * .10) + (num_pennies * .01)), 2)
    print("amount paid = ", paid_amt)

    if paid_amt >= MENU[coffeeType]["cost"]:
        change = round((paid_amt - MENU[coffeeType]["cost"]), 2)
        resources["money"] += MENU[coffeeType]["cost"]             # add money to machine
        print("{:.2f}".format(resources["money"]))
        format_change = "{:.2f}".format(change)
        print("Thank you. Here is your change. $ ", format_change)
        return True
    else:
        print("Sorry that's not enough money.")
        return False


def make_coffee():
    # resources["water"] = resources["water"] - MENU[coffeeType]["ingredients"]["water"]
    # resources["milk"] = resources["milk"] - MENU[coffeeType]["ingredients"]["milk"]
    # resources["coffee"] = resources["coffee"] - MENU[coffeeType]["ingredients"]["coffee"]

    for x in MENU[coffeeType]["ingredients"]:
        resources[x] = resources[x] - MENU[coffeeType]["ingredients"][x]


def print_report():
    print("Resource Report")
    print("---------------")
    print("Water: ", resources["water"], "ml")
    print("Milk: ", resources["milk"], "ml")
    print("Coffee: ", resources["coffee"], "g")
    print("Money: $", resources["money"])


while validItem:
    coffeeType = input("What would you like? (espresso/latte/cappuccino):")
    validItem = False
    for drink in MENU:
        if coffeeType == drink:
            validItem = True

    if debug:
        print(validItem)
        print(MENU)
        print("You ordered " + coffeeType)
        print(MENU[coffeeType])
        print(MENU[coffeeType]["cost"])
        print(MENU[coffeeType]["ingredients"]["water"])

    if validItem:
        enough_resources = check_resources()
        if enough_resources:
            print("==> before")
            print_report()                     # report before
            drink_paid = process_coins()
        else:
            print("Not enough supply")

        if drink_paid:
            make_coffee()
            print("==> after")
            print_report()                     # report after

    else:
        print("That is not a valid drink... goodbye!!")

