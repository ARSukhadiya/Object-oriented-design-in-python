import random

def show_menu():
    print("Menu:")
    print("1. Roll Dice")
    print("2. View Total Rolls")
    print("3. View Rolls Statistics")
    print("4. Exit")

def rolled_percentage(roll_count, total_rolls):
    roll_per = (roll_count / total_rolls) * 100
    if roll_per == 0:
        roll_per = 0
    else:
        roll_per = round(roll_per, 2)

    return roll_per

def calculate_roll_statistics(roll_count, total_rolls, explosions_count):

    for i in range(len(roll_count)):
        roll_count_i = roll_count[i]
        # roll_per = (roll_count[i] / total_rolls) * 100
        # roll_per = f"({(roll_count[i]) / total_rolls:.2%})"
        roll_per = rolled_percentage(roll_count[i], total_rolls)
        
        print(f"Number {i+1}: Rolled {roll_count_i} times ({roll_per}%)", end="")
        if i == 5:
            print(f" with {explosions_count} explosions!")
        
        print()

def main():
    print("Program to stimulate the roll of die.")

    show_menu()
    total_rolls = 0
    roll_count = [0] * 6
    explosions_count = 0

    while True:
        menu_choice = int(input("\nEnter your choice: "))
        
        if menu_choice == 1:
            while True:
                roll = random.randint(1, 6)
                total_rolls += 1
                roll_count[roll-1] += 1
                print("You rolled a {}!".format(roll), end="")

                if roll == 6:
                    explosions_count += 1
                    print("  The die explodes!")
                    print("(Rolling again for explosion...)")
                    continue
                else:
                    print()
                    break
        elif menu_choice == 2:
            print("Total rolls made:", total_rolls)
        elif menu_choice == 3:
            print("Roll statistics:")
            calculate_roll_statistics(roll_count, total_rolls, explosions_count)
        elif menu_choice == 4:
            print("Thanks for playing!")
            break
        else:
            print("Please enter the valid choice(1 to 4)")
            

if __name__ == "__main__":
    main()