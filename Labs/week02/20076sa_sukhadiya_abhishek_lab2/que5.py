"""
A program for printing a rectangle of the symbol
"""

def rectangle_of_symbol(height, weight, symbol):
    """
    Print a rectangle of the passed symbol
    """
    for i in range(height):
        for j in range(weight):
            print(symbol, end="")
        print()

def main():
    print("Print a rectangle of symbols")
    height = int(input("Enter the height: "))
    weight = int(input("Enter the weight: "))
    symbol = input("Enter the symbol: ")

    rectangle_of_symbol(height, weight, symbol)


if __name__ == "__main__":
    main()
