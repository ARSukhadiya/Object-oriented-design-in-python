def main():
    print("Program to check the string is palindrome or not")

    while True:
        input_str = input("\nEnter a five-character string: ")
        str_length = len(input_str)
        
        if str_length != 5:
            print("Error: Invalid input: Please enter a five-character string.")
            continue
        else:
            need_replace = 0
            replace_index = None
            replace_with_ch = None
            for str_index, reversed_index in zip(range(str_length+1), range(str_length-1, -1, -1)):
                if input_str[str_index] != input_str[reversed_index]:
                    need_replace += 1
                    if need_replace == 1:
                        replace_index = str_index
                        replace_with_ch = input_str[reversed_index]



            if need_replace == 0:
                print("{} is a palindrome.".format(input_str))
            elif need_replace == 2:
                revised_string = input_str.replace(input_str[replace_index], replace_with_ch, 1)
                print(f"{input_str} is not a palindrome. Replace character {replace_index + 1} with '{replace_with_ch}' to make it become a palindrome.")
                print("Revised string with uppercase: {}".format(revised_string.upper()))
            else:
                print("{} is not a palindrome. No single character replacement can make it one.".format(input_str))


if __name__ == "__main__":
    main()