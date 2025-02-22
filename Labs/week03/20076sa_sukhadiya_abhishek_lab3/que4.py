def main():
    print("The Electronic Survey Program")
    menu = ["Pizza", "Hot Dog", "Ham", "Cheese"]
    votes = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
    ]

    while True:
        for i in range(len(menu)):
            vote = input(f"Do you like {menu[i]} (y/n): ").lower()
            
            if vote == 'y':
                votes[i][0] += 1
            else:
                votes[i][1] += 1
        
        cont = input("\nDo you have another student (y/n)? ")
        if cont.lower() != 'y':
            break

    # print the result
    print(votes)
    print("\t\t\tLike\tDislike")
    for i in range(len(menu)):
        print(f"{menu[i]}\t\t\t{votes[i][0]}\t{votes[i][1]}")

if __name__ == "__main__":
    main()
