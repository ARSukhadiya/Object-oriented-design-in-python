# The program title
print("Check if a string is a palindrome")

str = input("Please enter a string: ")

left_index = 0
right_index = len(str) - 1

while left_index < right_index:
    if str[left_index] != str[right_index]:
        # Not a palindrome
        break

    left_index += 1
    right_index -= 1

if left_index < right_index:
    print("The", str, "is NOT a palindrome")
else:
    print("The", str, "is a palindrome")
