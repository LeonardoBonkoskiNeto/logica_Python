#########Simple Calculator################
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("This is not a value number. Please try again")

while True:
    n1 = get_number("type number one: ")
    n2 = get_number("type number two: ")
    operation = input("choose your operation ( +, -, /, *): ")

    if operation == "+":
        print(n1 + n2)
    
    elif operation == "-":
        print(n1 - n2)

    elif operation == "/":
        print(n1 / n2)

    elif operation == "*":
        print(n1 * n2)

    else:
        print("Error.")
    
    answer = input("do another operation?(y/n): ")
    if answer.lower() == "n":
        print("Operation completed")
        break