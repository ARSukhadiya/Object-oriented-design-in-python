"""
A program to sort a list and print unique values
"""

def main():
    print("Printing a list program")

    """
    Task 1
    """
    word_list = []
    while True:
        word = input("Enter a word: ")

        if word.lower() == 'exit':
            break
        
        word_list.append(word)

    print("\nThe original list: \n", word_list)
    print("\nThe sorted list: \n", sorted(word_list))

    """
    Task 2
    """
    print("\nThe unique words:")
    
    for i in range(len(word_list)):
        print_yes = True
        for j in range(i):
            if word_list[i] == word_list[j]:
                print_yes = False
                break
        
        if print_yes:
            print(word_list[i], end=', ')
    
    print("\b\b ")

if __name__ == "__main__":
    main()
