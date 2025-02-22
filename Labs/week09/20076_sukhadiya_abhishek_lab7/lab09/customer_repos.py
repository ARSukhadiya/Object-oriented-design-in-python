from customers import Customer
import csv

class CustomerRepository:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def save_customers(self, customers: list[Customer]):
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file)
            for customer in customers:
                writer.writerow(customer.convert_to_list())

    def read_customers(self) -> list[Customer]:
        customers: list[Customer] = []
        with open(self.__filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                customer = Customer(row[0], row[1], row[2], float(row[3]))
                customers.append(customer)
        return customers


def main():
    customers: list[Customer] = []
    customers.append(Customer("1111", "Lee", "Peter", 10000))
    customers.append(Customer("2222", "Tonn", "Tim", 9990))
    customers.append(Customer("3333", "Wu", "Nancy", 7000))
    customers.append(Customer("4444", "Buck", "Carl", 17700))
    repos = CustomerRepository("customers.csv")
    repos.save_customers(customers)

    customers2 = repos.read_customers();
    print(customers2)

if __name__ == "__main__":
    main()