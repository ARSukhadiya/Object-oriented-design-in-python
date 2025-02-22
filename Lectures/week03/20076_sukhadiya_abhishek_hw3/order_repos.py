from order import Order
import csv

class OrderRepository:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def save_orders(self, orders: list[Order]):
        with open(self.__filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for order in orders:
                writer.writerow(order.convert_to_list())

    def read_orders(self) -> list[Order]:
        orders: list[Order] = []
        with open(self.__filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                order = Order(row[0], row[1])
                orders.append(order)
        return orders


def main():
    order1 = Order("Stephen", 2005)


    order2 = Order("Bob", 2006)

    orders: list[Order] = []
    orders.append(order1)
    orders.append(order2)

    repos = OrderRepository("orders.csv")
    repos.save_orders(orders)

    orders2 = repos.read_orders()
    for order in orders2:
        print(order)


if __name__ == "__main__":
    main()
