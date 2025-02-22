MIN_SCORE = 0
MAX_SCORE = 10

def get_score_list():
    
    while True:
        score_str_list = input(f"\nEnter a list of number between {MIN_SCORE} and {MAX_SCORE} seperate a space: ").split()
        score_list = []
        valid = True

        print('score_str_list:', score_str_list)
        for score in score_str_list:
            score = int(score)
            score_list.append(score)

            if score < MIN_SCORE or score > MAX_SCORE:
                print(f"Error: Invalid input'{score}': put of range({MIN_SCORE}, {MAX_SCORE}).") 
                valid = False
        
        if not valid:
            continue   
        
        return score_list

def process_score(score_list):
    smallest = MAX_SCORE + 1
    largest = MIN_SCORE - 1
    sum = 0

    for score in score_list:
        if score < smallest:
            smallest = score
        if score > largest:
            largest = score

        sum += score
    
    average = sum / len(score_list)

    # Build the frequency list based on the score range 0 to 10
    freq = [0] * (MAX_SCORE - MIN_SCORE + 1)

    # scan the score list
    for score in score_list:
        freq[score] += 1
    
    mode = 0

    for i in range(len(freq)):
        if freq[i] > freq[mode]:
            mode = i

    return smallest, largest, sum, average, mode


def show_menu():
    print("\n--- MENU ---")
    print("1. Find the smallest score: ")
    print("2. Find the largest score: ")
    print("3. Find the total scores: ")
    print("4. Find the average score: ")
    print("5. Find the mode (most frequent) score: ")
    print("6. Exit")

def main():
    print("Find the smallest, largest, sum, average, mode")
    
    score_list = get_score_list()

    smallest, largest, sum, avg, mode = process_score(score_list)

    while True:
        show_menu()
        menu_option = int(input("Enter your choice: "))

        if menu_option == 1:
            print("\nThe smallest score is:", smallest)
        elif menu_option == 2:
            print("\nThe largetst score is:", largest)        
        elif menu_option == 3:
            print("\nTotal score is:", sum)        
        elif menu_option == 4:
            print("\nThe average score is:", avg)        
        elif menu_option == 5:
            print("\nThe mode score is:", mode)        
        elif menu_option == 6:
            print("\nBye!")
            break
        
        else:
            print("\nError: Invalid input!")
            continue


if __name__ == "__main__":
    main()
