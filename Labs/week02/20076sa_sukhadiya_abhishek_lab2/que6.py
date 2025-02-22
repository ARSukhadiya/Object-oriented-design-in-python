"""
A program for printing a triangle of the symbol
"""

def triangle_of_symbol(height, symbol):
    """
    Print a triangle of the passed symbol
    """
    for i in range(1, height+1):
        print(" " * (height-i), end="")
        print(symbol*(2*i-1))

def main():
    print("Print a triangle of symbols")
    height = int(input("Enter the height: "))
    symbol = input("Enter the symbol: ")

    triangle_of_symbol(height, symbol)

if __name__ == "__main__":
    main()
