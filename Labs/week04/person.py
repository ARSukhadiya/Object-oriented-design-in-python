class Hand:
    def __init__(self, fingers: int) -> None:
        self.__fingers= fingers

    def __str__(self) -> str:
        return f"Hand fingers={self.__fingers}"


class Person:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age
        self.salary = 100000

        # Composition - the object should be created inside the class
        self.__lhand = Hand(5)
        self.__rhand = Hand(5)

    # def set_age(self, age) -> None:
    #     self.__age = age

    # def get_age(self) -> int:
    #     return self.__age
    
    @property
    def age(self) -> int:               # getter
        return self.__age
    
    @age.setter
    def age(self, age: int) -> None:    # setter
        self.__age = age

    @property
    def name(self, name: str) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    # Convert the object to a string
    def __str__(self) -> str:
        return f"Person name={self.__name}, age={self.__age}, salary={self.salary}, left-hand={self.__lhand}, right-hand={self.__rhand}"

    def __repr__(self) -> str:
        return str(self)
        # return self.__str__()
        
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Person):
            return __value.__name == self.__name and __value.__age == self.__age
        else:
            return False         

def main():
    p = Person("Peter", 30)
    p2 = Person("Peter", 30)
    print('\np == p2:', p == p2)

    # p.set(32)
    # p.age = 32

    person_list = [p, p2]
    print('person_list:', person_list)
    print('\np:', p)

    # print('\np:', str(p))
    # print('\np:', p.__str__())

    print()
    # p.set_age(31)
    # print(p)
    # p.salary = 300000

    # print(p.get_age())

if __name__ == "__main__":
    main()
