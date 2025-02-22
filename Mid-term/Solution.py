from abc import ABC, abstractmethod
from enum import Enum

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class ProductType(Enum):
    ELECTRONICS = 1
    HARDWARE = 2
    FURNITURE = 3

class Product(Displayable):
    def __init__(self, product_id, product_name, model, product_type, base_price) -> None:
        self.__product_id: int = product_id
        self.__product_name: str = product_name
        self.__model: str = model
        self.__product_type: ProductType = product_type
        self.__base_price: float = base_price

    @property
    def base_price(self):
        return self.__base_price

    @property
    def product_type(self):
        return self.__product_type

    def __str__(self) -> str:
        output = f"Product_id = {self.__product_id}, Product_name = {self.__product_name}, Model = {self.__model}, Product_type = {self.__product_type}, Base_price = {self.__base_price}"
        return output
    
    @abstractmethod
    def get_final_price(self) -> float:
        pass

    def display(self) -> None:
        print(self)

class Factory(Displayable):
    def __init__(self, factory_name) -> None:
        self.__factory_name: str = factory_name
        self.__products: list[Product] = []

    def __str__(self) -> str:
        output = f"factory_name = {self.__factory_name}"
        for product in self.__products:
            output += str(product)
        return output

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    # def get_top_three_expensive_products(self) -> list[Product]:
    #     top_three_prods = []
    #     max_price = 0

    #     for product in self.__products:
    #         if product.base_price > max_price:
    #             max_price = product.base_price
    #             top_three_prods.append(product)
        
    #     return [top_three_prods[-1], top_three_prods[-2], top_three_prods[-3]]

    # def get_all_computers_with_touch_screen(self) -> list[Computer]:
    #     return []


    # def remove_all_computers(self) -> None:
    #     for i in range(len(self.__products)):
    #         if self.__products[i].product_type == ProductType.HARDWARE:
    #             self.__products.pop(i)

    def display(self) -> None:
        print(self)

class VoltageType(Enum):
    AC = 1
    DC = 2

class PowerSupply(Product):
    def __init__(self, product_id, product_name, model, product_type, base_price, input_voltage_type, output_voltage, output_current, power) -> None:
        super().__init__(product_id, product_name, model, product_type, base_price)
        self.__input_voltage_type: VoltageType = input_voltage_type
        self.__output_voltage: float = output_voltage
        self.__output_current: float = output_current
        self.__power: float = power

    def __str__(self) -> str:
        output = super().__str__()        
        output += f"input_voltage_type = {self.__input_voltage_type}, output_voltage = {self.__output_voltage}, output_current = {self.__output_current}, power = {self.__power}"
        return output

    def get_final_price(self) -> float:
        return self.base_price * self.__output_voltage

    def display(self) -> None:
        print(self)


class Table(Product):
    def __init__(self, product_id, product_name, model, product_type, base_price,
                 surface_area, height, material, storage) -> None:
        super().__init__(product_id, product_name, model, product_type, base_price)
        self.__surface_area = surface_area
        self.__height = height
        self.__material = material
        self.__storage = storage
    
    def __str__(self) -> str:
        output = super().__str__()        
        output += f"surface_area = {self.__surface_area}, height = {self.__height}, material = {self.__material}, storage = {self.__storage}"
        return output

    def get_final_price(self) -> float:
        return self.base_price + 12000

    def display(self) -> None:
        print(self)


class StorageType(Enum):
    HDD = 1
    SSD = 2


class Computer(Product):
    def __init__(self, product_id, product_name, model, product_type, base_price, 
                 cpu, cpu_speed, memory_size, storage_type, cellular, touch_screen) -> None:
        super().__init__(product_id, product_name, model, product_type, base_price)
        self.__cpu: str = cpu
        self.__cpu_speed: float = cpu_speed
        self.__memory_size: int = memory_size
        self.__storage_type: StorageType = storage_type
        self.__cellular: bool = cellular
        self.__touch_screen: bool = touch_screen

    def __str__(self) -> str:
        output = super().__str__()        
        output += f"cpu = {self.__cpu}, cpu_speed = {self.__cpu_speed}, memory_size = {self.__memory_size}, storage_type = {self.__storage_type}, cellular = {self.__cellular}, touch_screen = {self.__touch_screen}"
        return output
    
    def compute(self) -> None:
        print("Compute method being called!")

    def get_final_price(self) -> float:
        return self.base_price + 23000

    def display(self) -> None:
        print(self)


class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass

class Drone(Flyable, Computer):
    def __init__(self, product_id, product_name, model, product_type, base_price, cpu, cpu_speed, memory_size, storage_type, cellular, touch_screen,
                 camera, max_flight_time, gps) -> None:
        super().__init__(product_id, product_name, model, product_type, base_price, cpu, cpu_speed, memory_size, storage_type, cellular, touch_screen)
        self.__camera = camera
        self.__max_flight_time = max_flight_time
        self.__gps = gps

    def __str__(self) -> str:
        output = super().__str__()        
        output += f"camera = {self.__camera}, max_flight_time = {self.__max_flight_time}, gps = {self.__gps}"
        return output
    
    def get_final_price(self) -> float:
        return self.base_price + 20000

    def record(self) -> None:
        print("record method is being called!")

    def fly(self) -> None:
        print("fly method is being called!")

    def display(self) -> None:
        print(self)

def main():

    # Drone
    drone1 = Drone(1, "Prod_1", "Model_1", ProductType.HARDWARE, 12000, 
                   "Intel D5", 4.5, 23000, StorageType.HDD, True, True,
                   "Sony Stan_1", 12.30, True)
    print("Drone1----------------\n", drone1)
    drone1.record()
    drone1.fly()
    drone1.display()
    print("\nDron get_final_price: ", drone1.get_final_price())

    # Computer
    computer1 = Computer(2, "Prod_4", "Model_4", ProductType.HARDWARE, 52000, 
                   "Intel Core i5", 4.5, 23000, StorageType.HDD, True, True)
    print("Computer1----------------\n", drone1)
    computer1.compute()
    computer1.display()
    print("computer1.get_final_price:", computer1.get_final_price())


    # PowerSupply
    powersupply1 = PowerSupply(3, "Prod_2", "Model_2", ProductType.ELECTRONICS, 12000,
                               VoltageType.AC, 112.3, 111.1, 44.5)
    print("\n\npowersupply1----------------\n", powersupply1)
    powersupply1.display()
    print("\npowersupply1 get_final_price: ", powersupply1.get_final_price())

    # Table

    table1 = Table(4, "Prod_3", "Model_3", ProductType.HARDWARE, 12000,
                               12.3, 11.3, "Wooden", "Normal")
    print("\n\ntable1----------------\n", table1)
    table1.display()
    print("\ntable1 get_final_price: ", table1.get_final_price())

    factory1 = Factory("Famous factory")
    factory1.add_product(drone1)
    factory1.add_product(powersupply1)
    factory1.add_product(table1)

if __name__ == "__main__":
    main()