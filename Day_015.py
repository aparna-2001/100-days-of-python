# day_015
# Coffee Machine

# from data import MENU, resources

is_on = True
profit = 0

def is_order_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            is_enough =  False
        return is_enough

def process_coins():
    """
    :return: total money calculated from the coins
    """
    print("please insert coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry! that's not enough money. money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name} ☕")

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money :{profit}")
    else:
        drink = MENU[choice]
        if is_order_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(money_received = payment, drink_cost = drink['cost']):
                make_coffee(drink_name=choice, order_ingredients=drink['ingredients'])
