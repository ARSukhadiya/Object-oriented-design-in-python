from abc import ABC, abstractclassmethod
from typing import Any

class Person(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractclassmethod
    def dowork(self) -> None:
        pass

class Engineer(Person):
    def __init__(self, name, salary) -> None:
        super().__init__(name)
        self.salary = salary

    def dowork(self) -> None:
        print(f"{self.name} is designing a product", end="")

# class Professional_skills(Person):
#     def __init__(self, obj: Person) -> None:
#         self.obj = obj
#         self.skills = []

#     def add_skills(self, skill):
#         self.skills.append(skill)

class SoftwareDecorator(Person):
    def __init__(self, obj: Engineer) -> None:
        self.obj = obj

    def dowork(self) -> None:
        self.obj.dowork()
        print(", writing a program", end="")

class HardwareDecorator(Person):
    def __init__(self, obj: Engineer) -> None:
        self.obj = obj

    def dowork(self) -> None:
        self.obj.dowork()
        print(", designing a chip", end="")

class ConstructionDecorator(Person):
    def __init__(self, obj: Engineer) -> None:
        self.obj = obj

    def dowork(self) -> None:
        self.obj.dowork()
        print(", building a bridge")

def main():
    # p = Professional_skills(p)
    p = Engineer("Peter", 20000)
    print(type(p))
    p.dowork()

    print("\nDecorating the p object...")
    p = SoftwareDecorator(p)
    print(type(p))
    p.dowork()
    print()

    p = HardwareDecorator(p)
    print(type(p))
    p.dowork()
    print()

    # p = ConstructionDecorator(p)
    # p.dowork()


if __name__ == "__main__":
    main()