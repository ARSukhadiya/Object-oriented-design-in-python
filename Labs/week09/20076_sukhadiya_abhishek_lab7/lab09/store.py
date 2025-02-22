from customers import Customer
from customer_repos import CustomerRepository

class Store:
    def __init__(self, storename: str) -> None:
        self.__storename = storename
        self.__customers: list[Customer] = []

    @property
    def storename(self) -> str:
        return self.__storename

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index >= len(self.__customers) -1:
            raise StopIteration
        
        self.__index += 1
        return self.__customers[self.__index]

    def add_customer(self, customer: Customer):
        try:
            self.__customers.append(customer)

            # save latest customer data to DB
            self.save_customers_to_db()
            print("\nCustomer inserted successfully!")

        except Exception as exc:
            print("\n!Customer could not be Inserted")
            print("Exception:\n", exc)

    def display_customers(self, order: str = 'f'):
        print("\nAccount_no\t\tLastname\t\tFirstname\t\tBalance")
        if order in ['b', 'backward']:
            for i in range(len(self.__customers)-1, -1, -1):
                print(self.__customers[i])
        else:
            for customer in self.__customers:
                print(customer)
    
    def search_update_customer(self, customer_lastname: str, acc_bal: float) -> bool:
        if not self.search_customer(customer_lastname):
            print("\nCustomer account not found!")
            return False

        updated = False
        for customer in self.__customers:
            if customer.lastname == customer_lastname:
                customer.account_balance = acc_bal
                updated = True
                break

        if updated:
            # save latest customer data to DB
            self.save_customers_to_db()
            print('Record updated successfully!')

        return updated

    def remove_customer(self, account_no: int) -> bool:
        removed = False
        for i in range(len(self.__customers)):
            if int(self.__customers[i].account_no) == account_no:
                self.__customers.pop(i)
                removed = True
                break

        if removed:
            # save latest customer data to DB
            self.save_customers_to_db()
            print(f'Customer[acc_no = {account_no}] deleted successfully!')

        return removed

    def search_customer(self, lastname: str) -> list:
        # found = False
        found_customers = []
        for customer in self.__customers:
            if customer.lastname == lastname:
                # found = customer
                # found = True
                found_customers.append(customer)

        return found_customers

    def get_highest_lowest_balance_customers(self) -> tuple:
        higher_bal = 0
        lower_bal = 0

        for i in range(len(self.__customers)):
            if self.__customers[i].account_balance > higher_bal:
                higher_bal = self.__customers[i].account_balance
                highest_customer = self.__customers[i]

            if i == 0:
                lower_bal = self.__customers[i].account_balance

            if self.__customers[i].account_balance < lower_bal:
                lower_bal = self.__customers[i].account_balance
                lowest_customer = self.__customers[i]
        
        return highest_customer, lowest_customer


    def get_customers_from_db(self):
        repos = CustomerRepository("customers.csv")
        self.__customers = repos.read_customers()

    def save_customers_to_db(self):
        repos = CustomerRepository("customers.csv")
        repos.save_customers(self.__customers)