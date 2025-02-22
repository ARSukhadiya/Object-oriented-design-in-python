from store import Store
from customers import Customer

class StoreApp:
    def __init__(self) -> None:
        self.__store = Store("My Store")
        self.__store.get_customers_from_db()

    def show_title(self):
        print(f"The '{self.__store.storename}' Store Application")

    def show_menu(self):
        print("\n===== MENU ====")
        print("1. Add Customer")
        print("2. View all Customer")
        print("3. Edit Customer's Account Balance")
        print("4. Delete Customer")
        print("5. Search Customer")
        print("6. Customer with Highest and Lowest account balance")
        print("7. Exit")

    def scan_customer_details(self):
        while True:
            print("\nPlease enter the customer details: ")
            try:
                fname = input("First name: ")
                lname = input("Last name: ")
                acc_no = int(input("Account number/ID: "))
                acc_bal = float(input("Account balance(number): "))
                break
            except ValueError as exc:
                print("!Input Value is invalid!")
                print("Exception:" , exc)

        return acc_no, lname, fname, acc_bal

    def process_command(self, command) -> bool:
        cont = True

        if command == 1:            
            # Add customer
            
            customer = Customer(*self.scan_customer_details())
            self.__store.add_customer(customer)
        
        elif command == 2:
            # View all Customer
            
            display_order = input("Please enter the display-order (Forward / Backward, i.e. f / b): ").lower()
            self.__store.display_customers(display_order)
        
        elif command == 3:
            # Edit Customer-detail
            
            customer_lname = input("\nPlease enter the customer's Lastname to update the detail of: ")
            try:
                acc_bal = float(input("Enter the updated Account balance: "))
            except ValueError:
                print("Input Value is invalid!")

            if not self.__store.search_update_customer(customer_lname, acc_bal):
                print("Customer-record updation failed!")
        
        elif command == 4:
            # Delete Customer
            
            try:
                remove_acc_no = int(input("\nPlease enter the customer's Account-number to delete the account: "))
            except ValueError:
                print("Input Value is invalid!")
 
            if not self.__store.remove_customer(remove_acc_no):
                print("Customer-record deletion failed!")
        
        elif command == 5:
            # Search Customer
            
            search_last_name = input("\nPlease enter the customer's Lastname to search for: ")
            found_customers = self.__store.search_customer(search_last_name)
            if not found_customers:
                print("Customer not found!")
            else:
                print("\nAccount_no\t\tLastname\t\tFirstname\t\tBalance")
                for customer in found_customers:
                    print(customer)

        elif command == 6:
            # Customers with Highest and Lowest account-balance
            
            low, high = self.__store.get_highest_lowest_balance_customers()
            print(f"\nCustomer with Highest Account-balance: {low.name}")
            print(f"\nCustomer with Lowest Account-balance: {high.name}")

        elif command == 7:
            # Exit
            cont = False
        return cont


def main():
    app = StoreApp()
    app.show_title()

    cont = True
    while cont is True:
        app.show_menu()
        command = int(input("Enter your choice: "))
        cont = app.process_command(command)

if __name__ == "__main__":
    main()