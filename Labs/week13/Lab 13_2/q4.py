from abc import ABC, abstractmethod

class OrderTemplate(ABC):
    def process_order(self):
        self.greet_customer()
        self.take_order()
        self.prepare_order()
        if (self.want_special_packaging()):
            print("Decorating the wrapper...")
        self.serve_order()

    @abstractmethod
    def serve_order(self):
        pass

    def greet_customer(self):
        print("Hi Sir/Ma'am, Welcome.")

    def take_order(self):
        print("Taking the order...")

    def prepare_order(self):
        print("Preparing the order...")

    def want_special_packaging(self):
        return False

    
class DineInOrder(OrderTemplate):
    def __init__(self, order_no: int, table_no: int) -> None:
        self.__order_no: int = order_no
        self.__table_no: int = table_no

    def serve_order(self):
        self.serve_to_the_table()
    
    def serve_to_the_table(self):
        print(f"Serving the order[{self.__order_no}] to the table {self.__table_no}.")


class TakeOutOrder(OrderTemplate):
    def __init__(self, order_no: int, counter_no: int) -> None:
        self.__order_no: int = order_no
        self.__counter_no: int = counter_no

    def serve_order(self):
        self.wrap_order()
        self.give_order_customer()

    def wrap_order(self):
        print(f"Wrapping the order[{self.__order_no}].")

    def want_special_packaging(self):
        ans = input("Would you like to have special packaging (y/n)?")
        if ans in "yY":
            return True
        else:
            return False
    
    def give_order_customer(self):
        print(f"Giving the wrapped-order[{self.__order_no}] to the counter {self.__counter_no}.")


def main():
    order1 = DineInOrder(order_no=1, table_no=4)
    order2 = DineInOrder(order_no=2, table_no=10)
    order3 = TakeOutOrder(order_no=3, counter_no=2)
    order4 = TakeOutOrder(order_no=4, counter_no=2)

    order1.process_order()

    print()
    order2.process_order()

    print()
    order3.process_order()

    print()
    order4.process_order()


if __name__ == "__main__":
    main()
