def main():
    print("Merges two sorted lists")

    # Get the both array form the user in string format
    list_1_str = input("Enter the values of list one (seperate a space - In the ascending order) : ").split()
    list_2_str = input("Enter the values of list two (seperate a space - In the ascending order) : ").split()

    # Update the value in the int formate
    list1 = [int(list_1_item) for list_1_item in list_1_str]
    list2 = [int(list_2_item) for list_2_item in list_2_str]

    # Result list
    i = 0
    j = 0
    res_list = []

    # Process to find and add the data in the result list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            # res_list.append(list1[i])
            list2.insert(j, list1[i])
            i += 1
        else:
            # res_list.append(list2[j])
            list2.insert(j, list2[j])
            j += 1
    # output (concat the remain list values)
    print("result : ", res_list + list1[i:] + list2[j:])


if __name__ == "__main__":
    main()
