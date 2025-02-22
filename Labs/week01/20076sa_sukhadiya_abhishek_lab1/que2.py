# The program title
print("Format the String")


# Get a string input
str_input = input("Enter a string: ").lower()
formatted_str = ""

for i in range(len(str_input)):
    if ord(str_input[i]) >= 97:
        formatted_str += chr(ord(str_input[i])-32)
    else:
        formatted_str += str_input[i]

    if i == len(str_input)-1: 
        formatted_str += '.'

print('\nFormatted string:', formatted_str)