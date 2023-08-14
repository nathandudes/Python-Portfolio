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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True


def is_sufficient(order_ingredients):
    """RETURNS TRUE IF ORDER CAN BE. FALSE IF INSUFFICIENT"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}")
            return False
    return True


def transaction(money_received, drink_cost):
    """Return True when the payment is accepted, or False if the money is insufficient"""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}")
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded")
        return False


def calculate():
    """RETURNS TOTAL CALCULATED FROM MONEY INSERTED"""
    print("Please insert coins.")
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.10
    total += float(input("How many nickles?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    print(f"Money added to machine: ${total}")
    return total


def make_coffe(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == 'off':
        is_on = False
    elif order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[order]
        print(f"Your {order} will be {drink['cost']}")
        if is_sufficient(drink['ingredients']):
            payment = calculate()
            if transaction(payment, drink['cost']):
                make_coffe(order, drink['ingredients'])
