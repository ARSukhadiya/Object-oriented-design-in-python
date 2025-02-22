from abc import ABC, abstractmethod
from typing import Optional

class Product(ABC):
    def __init__(self) -> None:
        print("Product")
        # super().__init__()

class Computer(Product):
    def __init__(self) -> None:
        print("Computer")
        # super().__init__()


class Radio(Product):
    def __init__(self) -> None:
        print("Radio")
        # super().__init__()



class ProductFactory:

    @staticmethod
    def get_product(type: str) -> Optional[Product]:
        if type == "Computer":
            return Computer()
        elif type == "Radio":
            return Radio()
        return None

def main():
    # obj = Computer()          create dependency
    type = input("Enter product type:")
    obj = ProductFactory.get_product(type)

    print(type(obj))


if __name__ == "__main__":
    main()