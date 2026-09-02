#day 010
#Calculator project

from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


num1 = float(input("Enter the first number: "))

symbols = ["+", "-","*","/"]
for symbol in symbols:
    print(symbol)

should_continue = True

while should_continue:
    pick_an_operation = input("Pick an operation: ")
    if pick_an_operation == "+":
        result = operators_dict["+"](num1, int(input("What is the second number: ")))
        print(result)
    elif pick_an_operation == "-":
        result = operators_dict["-"](num1, int(input("What is the second number: ")))
        print(result)
    elif pick_an_operation == "*":
        result = operators_dict["*"](num1, int(input("What is the second number: ")))
        print(result)
    elif pick_an_operation == "/":
        result = operators_dict["/"](num1, int(input("What is the second number: ")))
        print(result)
    else:
        print("invalid input")

    restart = input(f"Type 'y' to calculate with {result} or 'n' to continue with new calculation or 'e' to end the program: ").lower()
    if restart == "y":
        num1 = result
        should_continue = True
    elif restart == "n":
        num1 = float(input("Enter the number: "))
        should_continue = True
    elif restart == "e":
        should_continue = False
        print("Goodbye")
