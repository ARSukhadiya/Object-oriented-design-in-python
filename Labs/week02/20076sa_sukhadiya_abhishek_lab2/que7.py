"""
A program for printing a circle of the symbol
"""

def is_pos_in_circle(x, y, radius):
    """
    Calculate and return (true/false) according to the pixel's position in a circle or not 
    """
    return (x * x + y * y) <= (radius * radius)

def circle_of_symbols(radius, symbol):
    """
    Print a circle of the passed symbol
    """
    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            if is_pos_in_circle(x, y, radius-0.4):
                print(symbol, end=' ')
            else:
                print(" ", end=' ')
        print()

def main():
    print("Print a circle of symbols")
    radius = int(input("Enter the radius: "))
    symbol = input("Enter the symbol: ")
    circle_of_symbols(radius, symbol)


if __name__ == "__main__":
    main()
