from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

math_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for key in math_dict:
        print(key)

    again = 'y'
    answer = num1

    while again == 'y':
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer2 = math_dict[operation_symbol](answer, num2)
        print(f"{answer} {operation_symbol} {num2} = {answer2}")
        again = input(f"Type 'y' to continue calculating with  {answer2}, or type 'n' to start a new calculator: ")
        if again == 'y':
            answer = answer2
        elif again == 'n':
            calculator()
        else:
            return

calculator()
