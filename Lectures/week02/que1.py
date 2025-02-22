def hello():
    print('hellop')


def traslate_char_to_digit(letter):
    """
    Translate the letter and return the correspoding decoded_number
    """
    sets = [[1, "ADGJM"],
            [2, "EFTUV"],
            [3, "BEKLO"],
            [4, "HSWXY"],
            [5, "CFNPQ"],
            [6, "IYZ"],
            [7, "HIRST"],
            [8, "Z"]
    ]

    decoded_number = None
    for letters_set in sets:
        if letter in letters_set[1]:
            decoded_number = letters_set[0]
    
    return decoded_number


def main():
    print("Program for cryptic-key code-breaking")

    while True:
        print("\nPrompt: Enter a letter to decipher:")
        letter = input("User input: ")
        if len(letter) > 1:
            print("Please enter only one letter/character!")
            continue 
        print(f"Program output: You entered: {letter}")

        # Get the cryptic decoded-number
        if 65 <= ord(letter) and ord(letter) <= 90:
            print(f"The corresponding digit is {traslate_char_to_digit(letter)}")
        else:
            print('No matching digit exists for this character!')


if __name__ == "__main__":
    main()