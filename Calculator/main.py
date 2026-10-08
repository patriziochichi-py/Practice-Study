def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

from art import logo
print(logo)

def calculator():
    should_accumulate = True
    n1 = float(input("Type your first number and press enter: "))

    while should_accumulate:
        operation = input("+\n"
                      "-\n"
                      "*\n"
                      "/\n"
                      "Type a mathematical operation symbol: ")
        n2 = float(input("Type another number and press enter: "))
        answer = calculator_dict.get(operation)(n1, n2)
        print(f"{n1} {operation} {n2} = {answer}")

        cont_calcul = input(f"Press 'y' to continue calculating with {answer}, or 'no' to start a new calculation: ")

        if cont_calcul == "y":
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 50)
            calculator()

calculator()