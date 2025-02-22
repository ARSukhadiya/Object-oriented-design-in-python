from abc import ABC, abstractmethod
from typing import Optional

class Vehicle(ABC):
    def __init__(self) -> None:
        print("Vehicle")


class Sedan(Vehicle):
    def __init__(self) -> None:
        print("Sedan")


class Truck(Vehicle):
    def __init__(self) -> None:
        print("Truck")


class VehicleFactory:
    vehicle = [1, 2,3]
    # def __init__(self, factory_name) -> None:
    #     self.__factory_name = factory_name

    # def get_vehicle(self, type: str) -> Optional[Vehicle]:
    #     print(f"{self.__factory_name} is making a product...")
    #     print('---', self.vehicle)
    #     if type == "Sedan":
    #         return Sedan()
    #     elif type == "Truck":
    #         return Truck()
        # return None

    @staticmethod
    def get_vehicle(type: str) -> Optional[Vehicle]:
        if type == "Sedan":
            return Sedan()
        elif type == "Truck":
            return Truck()
        return None


def main():
    # obj = Computer()          create dependency
    type = input("Enter product type:")

    obj = VehicleFactory.get_vehicle(type)
    # obj = VehicleFactory("Factory_1").get_vehicle(type)

    # print(type(obj))


if __name__ == "__main__":
    main()