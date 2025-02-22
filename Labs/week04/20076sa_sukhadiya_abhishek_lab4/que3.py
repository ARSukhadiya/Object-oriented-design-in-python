
class Employee:
    def __init__(self, name: str, emp_id: int, dept_no: int, age: int) -> None:
        self.__name = name
        self.__id = emp_id
        self.dept_no = dept_no
        self.age = age
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def emp_id(self) -> int:
        return self.__id
      
    def __str__(self) -> str:
        return f"Employee: name = {self.__name}, id = {self.__id}, dept_no = {self.dept_no}, age = {self.age}"


class Company:
    def __init__(self, id: int, name: str) -> None:
        self.__id = id
        self.__name = name
        self.employees = []

    def add_employee(self, new_employee: Employee):
        duplicate_emp = False

        for employee in self.employees:
            if employee.emp_id == new_employee.emp_id:
                duplicate_emp = True
        
        if duplicate_emp:
            print("\nEmployee-id already exists!")
        else:
            self.employees.append(new_employee)
            print("Employee added successfully!")

    def remove_employee(self, remove_employee: Employee):
        emp_removed = False
        for employee in self.employees:
            if employee.emp_id == remove_employee.emp_id:
                self.employees.remove(remove_employee)
                emp_removed = True

        if not emp_removed:
            print("\nEmployee couldn't found!")
        else:
            print("Employee removed successfully!")

    def display_all_employees(self):
        print("{:18}|{:15}|{:20}|{:15}".format("Employee Name", "Employee Id", "Department Number", "Age"))
        print("-" * 68)
        
        for employee in self.employees:
            print("{:18}|{:15}|{:20}|{:15}".format(employee.name, str(employee.emp_id), str(employee.dept_no), str(employee.age)))
        
        print("-" * 68)

    def display_employee(self, emp_id: int):
        emp_found = False
        print("\n{:18}|{:15}|{:15}|{:15}".format("Employee Name", "Employee Id", "Department Number", "Age"))
        print("-" * 53)

        for employee in self.employees:
            if employee.emp_id == emp_id:
                emp_found = True
                print("{:18}|{:10}|{:15}|{:10}".format(employee.name, str(employee.emp_id), str(employee.dept_no), str(employee.age)))

        print("-" * 53, '\n')
        return emp_found

    def __str__(self) -> str:
        result = f"Company: id = {self.__id}, name = {self.__name}\n"
        for employee in self.employees: 
            result += f"{employee}\n"
        
        return result
        
def menu():

    print("\nWhat would you like to do! ")
    print("e - Enter a new employee's information")
    print("a - Display all employees information")
    print("d - Display an employee's information")
    print("q - Quit")


def main():
    print("\n--- Employee Management ---")
    company1 = Company(1, "BrainTechs")

    while True:
        # Menu
        menu()
        choice = input("(e/a/d/q)> ").strip()
        print()

        if choice == 'e':
            name = input("Name: ")
            id = int(input("Employee id: "))
            dept_no = int(input("Department-number: "))
            age = int(input("Age: "))
            company1.add_employee(Employee(name, id, dept_no, age))
            
        elif choice == 'a':
            company1.display_all_employees()

        elif choice == 'd':
            while True:
                emp_id = int(input("\nEnter Employee-id to find: "))
                if not company1.display_employee(emp_id):
                    print("Employee not found!")
                    
                    retry = input("Do you want to retry (y/n)?:").strip()
                    if retry != "y":
                        break
                    else:
                        continue
                break

        elif choice == 'q':
            return 0


if __name__ == "__main__":
    main()
