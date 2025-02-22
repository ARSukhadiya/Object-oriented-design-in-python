"""
A Program to implement a simple calculator
"""

def main():
    print("A simple Calculator program")

    while True:
        num1= int(input("Enter number_1:"))
        num2= int(input("Enter number_2:"))
        operator = input("Enter the operator:")

        error_msg = None
        result = None

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            error_msg = "Error! Invalid operator"

        if error_msg is None:
            print("The result =", result)
        else:
            print(error_msg)

        confirm = input("Do you want to continue (y/n)? ")
        if confirm.lower() != 'y':
            break


if __name__ == "__main__":
    main()
