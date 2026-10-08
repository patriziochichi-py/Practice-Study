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
PROFIT = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1: print a report of all the machine resources by typing "report"
# TODO 2: resources sufficient to make a drink
# TODO 3: the machine should turn off when typing "off"
# TODO 4: prompt user "what would you like?" everytime an action is completed
# TODO 5: process all the kinds of coins
# TODO 6: if the money is enough, make the coffee. if not, say sorry and refund
# TODO 7: make the coffee and deplete the resources
# TODO 8: if the user asks a report again, the resources should be lower
# TODO 9: if there aren't enough resources the machine should say "sorry, not enough xxx"

def is_resource_enough(order_ingredient):
    """This function returns a comparison between the ingredients and the machine resource"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """this function returns the sum of all the coins inserted into the machine"""
    print("please insert coins")
    total_cash = int(input("How many quarters?: ")) * 0.25
    total_cash += int(input("How many dimes?: ")) * 0.1
    total_cash += int(input("How many nickles?: ")) * 0.05
    total_cash += int(input("How many pennies?: ")) * 0.01
    return total_cash

def is_transaction_successful(money_received, drink_cost):
    """this function returns True if the payment is successful, False if not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"This is your change ${change}")
        global PROFIT
        PROFIT += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredient):
    """deduct the drink ingredients from the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"here is your {drink_name} ")

machine_off = False

while not machine_off:
    user_input = input("What would you like to order? (espresso 1.5$/latte 2.5$/cappuccino 3.0$): ").lower()
    if user_input == "off":
        machine_off = True

    elif user_input == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")

    else:
        drink = MENU[user_input]
        if is_resource_enough(drink["ingredients"]):
            user_payment = process_coins()
            if is_transaction_successful(user_payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])