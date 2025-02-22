def show_menu():
    print("\n\n--- MENU ---")
    print("1. Enter a new employee information (name, id, dept_no, age): ")
    print("2. Display all employee information")
    print("3. Find employees' information by name")
    print("4. Disaply all employees' information in chronological order by age")
    print("5. Remove the employee by ID")
    print("6. Quit")
    

def main():
    employee_list = []

    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
    
        if choice == 1:
            name = input("Enter the employee name: ")
            id = int(input("Enter the employee id: "))
            dept_no = int(input("Enter the department number: "))
            age = int(input("Enter the employee age: "))
            # name = "aaaassa"
            # id = 123
            # dept_no = 11
            # age = 30
            employee_list.append([name, id, dept_no, age])
    
        elif choice == 2:
            print("\n" + "-"*53)
            print("{:18}|{:10}|{:15}|{:10}".format('Employee_Name', 'ID', 'Department_No', 'Age'))
            print("-" * 53)

            for employee in employee_list:
                print("{:18}|{:10}|{:15}|{:10}".format(employee[0], str(employee[1]), str(employee[2]), str(employee[3])))
            
            print("-" * 53)

        elif choice == 3:
            while True:
                find_name = input("Enter the name of the employee: ")
                found = False

                print("\n" + "-"*53)
                print("{:18}|{:10}|{:15}|{:10}".format('Employee_Name', 'ID', 'Department_No', 'Age'))
                print("-" * 53)

                for employee in employee_list:
                    if employee[0] == find_name:
                        found = True
                        print("{:18}|{:10}|{:15}|{:10}".format(employee[0], str(employee[1]), str(employee[2]), str(employee[3])))
                print("-" * 53)

                if found:
                    break
                else:
                    print("Requested employee not found!")

        elif choice == 4:
            print("\n" + "-"*53)
            print("{:18}|{:10}|{:15}|{:10}".format('Employee_Name', 'ID', 'Department_No', 'Age'))
            
            for employee in sorted(employee_list, key=lambda x: x[3], reverse=True):
                print("{:18}|{:10}|{:15}|{:10}".format(employee[0], str(employee[1]), str(employee[2]), str(employee[3])))
            
            print("-" * 53)

        elif choice == 5:
            emp_id = int(input("Enter the ID of the employee to remove: "))
            for i, item in enumerate(employee_list):
                if int(item[1] == emp_id):
                    employee_list.pop(i)
                    print("\nEmployee deleted successfully")

        elif choice == 6:
            confirm = input("Do you want to Exit(y/n)? ")
            if confirm.lower() != 'y':
                print("Good bye!")
                break

        else:
            print("\nError: Invalid choice!")


if __name__ == "__main__":
    main()
