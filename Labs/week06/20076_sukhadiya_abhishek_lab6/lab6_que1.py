from abc import ABC, abstractmethod
from typing import Any

class Disaplyable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass

class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass

class Part(Disaplyable):
    def __init__(self, partno: int, price: float) -> None:
        self.__partno = partno
        self.__price = price
    
    def __str__(self) -> str:
        return f"partno = {self.__partno}\nprice = {self.__price}\n"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Part):
            return self.__partno == __o.__partno
        else:
            return False

    def display(self) -> None:
        print(self)

    @property
    def partno(self) -> int:
        return self.__partno

    @property
    def price(self) -> float:
        return self.__price
    

class JetFighter(Disaplyable, Flyable):
    def __init__(self, model: str, speed: int) -> None:
        self.__model = model
        self.__speed = speed

    def __str__(self) -> str:
        return f"model = {self.__model}\nspeed = {self.__speed}"
    
    def display(self) -> None:
        print(self)

    def fly(self) -> None:
        print(f"The JetFigher {self.__model} is flying in the sky!")

class MovablePart(Movable, Part):
    def __init__(self, partno: int, price: float, type: str) -> None:
        Part.__init__(self, partno, price)
        self.__type = type

    @property
    def type(self) -> str:
        return self.__type
    
    def __str__(self) -> str:
        return Part.__str__(self) + f"type = {self.__type}\n"
    
    def display(self) -> None:
        print(self)

    def move(self) -> None:
        print(f"partno: {self.partno} is moving fast!")


class Machine(Disaplyable):
    def __init__(self, machine_name: str) -> None:
        self.__machine_name = machine_name
        self.__parts: list[Part] = []

    def add_part(self, part: Part) -> None:
        self.__parts.append(part)

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index >= len(self.__parts) -1:
            raise StopIteration
        
        self.__index += 1
        return self.__parts[self.__index]

    def __str__(self) -> str:
        output = f"machine_name = {self.__machine_name}\n"
        output += "The machine has these parts:\n"
        for part in self.__parts:
            output += str(part) + "\n\n"
        return output
    
    def display(self) -> None:
        print(self)

    @abstractmethod
    def dowork(self) -> None:
        pass

    @property
    def machine_name(self) -> str:
        return self.__machine_name
    
    def get_movable_parts(self) -> list[MovablePart]:
        return_list: list[MovablePart] = []
        for part in self:
            if isinstance(part, MovablePart):
                return_list.append(part)
        return return_list


    def remove_part(self, partno: int) -> None:
        target_part: Part = Part(partno, 0)
        self.__parts.remove(target_part)

    
    # Return a dictionary of items(key=partno, value=occurences)
    def find_duplicated_parts(self) -> dict[int, int]:
        part_freq: dict[int, int] = {}

        for part in self.__parts:
            if part.partno in part_freq:
                part_freq[part.partno] += 1
            else:
                part_freq[part.partno] = 1

        duplicated_parts: dict[int, int] = {}
        for partno, times in part_freq.items():
            if times > 1:
                duplicated_parts[partno] = times

        return duplicated_parts


class Robot(Machine, JetFighter):
    def __init__(self, machine_name: str, cpu: str, model: str, speed: int) -> None:
        Machine.__init__(self, machine_name)
        JetFighter.__init__(self, model, speed)
        self.__cpu = cpu

    def __str__(self) -> str:
        output = f"cpu = {self.__cpu}\n"
        output += Machine.__str__(self)
        output += JetFighter.__str__(self)
        return output
    
    def dowork(self) -> None:
        print(f"The Robot {self.machine_name} is assembling a big truck.")

    def fly(self) -> None:
        JetFighter.fly(self)
        print(f"The Robot {self.machine_name} is flying over the ocean!")
        
    def display(self) -> None:
        print(self)

    def __iter__(self):
        return Machine.__iter__(self)

    def get_expensive_parts(self, price_limit: int) -> list[Part]:
        expensive_parts: list[Part] = []

        self.__iter__()
        while True:
            try:
                part = self.__next__()
                if part.price >= price_limit:
                    expensive_parts.append(part)
            except StopIteration:
                break

        return expensive_parts
    
    def get_movable_parts(self) -> list[MovablePart]:
        return Machine.get_movable_parts(self)

    def get_movable_parts_bytype(self) -> dict[str, list[Part]]:
        movable_parts: dict[str, list[Part]] = {}

        for movable_part in self.get_movable_parts():
            if movable_part.type in movable_parts:
                movable_parts[movable_part.type].append(movable_part)
            else:
                movable_parts[movable_part.type] = [movable_part]

        return movable_parts


def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000) 
    robo.add_part(Part(111, 100)) 
    robo.add_part(Part(222, 200)) 
    robo.add_part(Part(333, 300)) 
    robo.add_part(Part(222, 300)) 

    robo.add_part(MovablePart(555, 300, "TypeA")) 
    
    robo.add_part(Part(111, 100)) 
    robo.add_part(Part(111, 100)) 
    
    robo.add_part(MovablePart(777, 300, "TypeB")) 
    robo.add_part(MovablePart(655, 300, "TypeA")) 
    robo.add_part(MovablePart(755, 300, "TypeA")) 
    robo.add_part(MovablePart(977, 300, "TypeB"))
    robo.display() 
    
    print() 
    print("\nRobot test flight----") 
    robo.fly() 
    
    print("\nRobot dowork() test ----") 
    robo.dowork() 
    
    print("\nDuplicated part list----") 
    partfreq = robo.find_duplicated_parts() 
    for partno in partfreq.keys(): 
        print(partno,'=>', partfreq[partno], 'times') 
    
    print("\nExpensive part list----") 
    expensive_parts = robo.get_expensive_parts(200) 
    for part in expensive_parts: 
        part.display() 
    
    print("\nMovable part list----") 
    movable_parts = robo.get_movable_parts_bytype() 
    for type, parts in movable_parts.items(): 
        print("type =", type) 
        for part in parts: 
            part.display() 
        print() 

    print("\nAsk movable to move----") 
    movable_parts = robo.get_movable_parts() 
    for part in movable_parts: 
        part.move() 
    
    print("\nTest remove_part() ----") 
    robo.remove_part(333) 
    for part in robo: 
        if part.partno == 333: 
            print('Found 333') 
            break

if __name__ == "__main__":
    main()