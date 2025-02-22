from abc import ABC, abstractclassmethod

class CalculatorInterface:
    @abstractclassmethod
    def add(self, x, y):
        pass

    @abstractclassmethod
    def subtract(self, x, y):
        pass

    @abstractclassmethod
    def price(self):
        pass

class BasicCalculator(CalculatorInterface):
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x-y

    def price(self):
        return 100


class CalDecorator(CalculatorInterface):
    def __init__(self, obj: BasicCalculator) -> None:
        self.__obj = obj

    @property
    def obj(self):
        return self.__obj

    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y

    def add(self, x, y):
        print(f"Adding {x=}, {y=}")    # enhance the existing function
        return self.__obj.add(x, y) 

    def subtract(self, x, y):
        print(f"Subtracting {x=}, {y=}")    # enhance the existing function
        return self.__obj.subtract(x, y) 

    def price(self):
        return self.__obj.price() + 50


class DisplayDecorator(CalDecorator):
    def display(self):
        print("I can display something now...")

    def price(self):
        return self.obj.price() + 20
    

def main():
    cal = BasicCalculator()
    # print(cal.add(10, 20))
    # print(cal.subtract(10, 20))

    print("\nDecorating the cal object...")
    cal = CalDecorator(cal)
    # print(cal.add(10, 20))
    # print(cal.subtract(10, 20))
    # print(cal.multiply(10, 20))
    # print(cal.divide(10, 20))

    print("\nDecorating the cal object...")
    cal = DisplayDecorator(cal)
    print(cal.multiply(10, 20))
    print(cal.divide(10, 20))
    print(cal.add(10, 20))
    print(cal.subtract(10, 20))
    cal.display()
    print(cal.price())

if __name__ == "__main__":
    main()