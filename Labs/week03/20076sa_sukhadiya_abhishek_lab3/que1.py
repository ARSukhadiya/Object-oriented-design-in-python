def calculate_hex(decimal_no):
    """
    Convert decimal to hexadecimal number
    """
    HEX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

    return HEX[decimal_no]


def main():
    print("Program to convert the decimal number to the hexadecimal number\n")

    while True:
        input_num = int(input("Enter a decimal value (0 to 15): "))
        
        if input_num < 0 or input_num > 15:
            print("Input out of range! \n")
            continue

        hex_no = calculate_hex(input_num)
        print("The hex value is {} \n".format(hex_no))

        confirm = input("Do you want to continue (y/n)? ")
        if confirm.lower() != 'y':
            break



if __name__ == "__main__":
    main()