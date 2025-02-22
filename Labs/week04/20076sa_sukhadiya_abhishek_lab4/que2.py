class Room:
    def __init__(self, type: str, size: int) -> None:
        self.__type = type 
        self.__size = size
    
    @property
    def type(self) -> str:
        return self.__type
    
    @type.setter
    def type(self, type: str) -> None:
        self.__type = type 
    
    @property
    def size(self) -> int:
        return self.__size 

    @size.setter
    def size(self, size:int ) -> None:
        self.__size = size
    
    def __str__(self) -> str:
        return f"Room: type = {self.__type}, size = {self.__size}"
    
class Garage():
    def __init__(self, type:str , size:int , door_type:str ):
        self.__type = type
        self.__size = size
        self.__door_type = door_type
    
    @property 
    def door_type(self) -> str:
        return self.__door_type
    
    @door_type.setter
    def door_type(self, door_type) -> None:
        self.__door_type = door_type
    
    def __str__(self) -> str:
        return f"Garage: type = {self.__type}, size = {self.__size}, door_type = {self.__door_type}"
    
class Television:
    def __init__(self, screen_type: str, screen_size: int, resolution: str, price: float):
        self.__screen_type = screen_type 
        self.__screen_size = screen_size
        self.__resolution = resolution
        self.__price = price
    
    @property
    def screen_type(self) -> str:
        return self.__screen_type
    
    @screen_type.setter
    def screen_type(self, screen_type) -> None:
        self.__screen_type = screen_type
    
    @property
    def screen_size(self) -> int:
        return self.__screen_size
    
    @screen_size.setter
    def screen_size(self, screen_size) -> None:
        self.__screen_size = screen_size
    
    @property
    def resolution(self) -> str:
        return self.__resolution
    
    @resolution.setter
    def resolution(self, resolution) -> None:
        self.__resolution = resolution
    
    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, price) -> None:
        self.__price = price

    def __str__(self) -> str:
        return f"Television: screen_type = {self.__screen_type}, screen_size = {self.screen_size}, resolution = {self.__resolution}, price = {self.__price}"

class House:
    def __init__(self, address: str, square_feet: int, garage: Garage):
        self.__address = address
        self.__square_feet = square_feet
        self.__garage = garage
        self.__rooms: list[Room] = []
        self.__televisions: list[Television] = []

    @property
    def address(self) -> str:
        return self.__address
    
    @address.setter
    def address(self, address) -> None:
        self.__address = address
    
    @property
    def square_feet(self) -> int:
        return self.__square_feet
    
    @square_feet.setter
    def square_feet(self, square_feet) -> None:
        self.__square_feet = square_feet
    
    @property
    def garage(self) -> Garage:
        return self.__garage
    
    @garage.setter
    def garage(self, garage) -> None:
        self.__garage = garage

    def __str__(self) -> str:
        result = f"House: address = {self.__address}, square_feet = {self.__square_feet}, garage = {str(self.__garage)}\n" 
        result += f"Rooms = [{','.join(map(str,self.__rooms)) }] \n"
        result += f"Televisions = [{','.join( map(str, self.__televisions))}]"
        return result
    
    def add_room(self, type: str, size: int) -> None:
        if len(self.__rooms) >= 4:
            print("No more room for additional rooms in the house!")
            return 
        
        self.__rooms.append(Room(type, size))

    def add_tv(self, screen_type: str, screen_size: int, resolution: str, price: float) -> None:
        self.__televisions.append(Television(screen_type, screen_size, resolution, price))

    def remove_tv(self, screen_type: str, screen_size: int, resolution: str) -> None:
        for i in range(len(self.__televisions)):
            if (self.__televisions[i].screen_type, self.__televisions[i].screen_size, self.__televisions[i].resolution) == (screen_type, screen_size, resolution):
                self.__televisions.pop(i)
                return
    
    def change_garage_size(self, size: int) -> None:
        self.garage.size = size 

    def get_biggest_room(self) -> Room:
        return max(self.__rooms, key = lambda x : x.size)
    
    def get_oled_televisions(self) -> list[Television]:
        tvs: list[Television] = []

        for television in self.__televisions:
            if television.screen_type == "oled":
                tvs.append(television)
        
        return tvs    

    def is_similar_house(self, other) -> bool:
        return self.__square_feet == other.square_feet and len(self.__rooms) == len(other.__rooms)


def main():
    print("\nTest the classes created.")
    room1 = Room("Living", 400)
    print(room1)
    
    garage = Garage("Single", 200, "Bike")
    print(garage)

    house = House("201 Crade Lane", 1000, garage)
    house.add_room("Bedroom1", 400)
    house.add_room("Bedroom2", 300)
    house.add_room("Bathroom", 100)
    house.add_room("Living", 200)
    print(house)

    print("\nAdd one more room:")
    house.add_room("Storage", 300)
    house.add_tv("lcd", "55", "4K", 800)
    house.add_tv("lcd", "32", "1080p", 500)
    house.add_tv("oled", "72", "8K", 1000)
    print(house)

    print("\nThe get_biggest_room:")
    print(house.get_biggest_room())

    print("\nThe get_oled_televisions function:")
    for television in house.get_oled_televisions():
        print(television)

    print("\nTest the is_similar_house function:")
    house2 = House("661 Bakers Street", 1500, garage)
    house2.add_room("room1",1)
    house2.add_room("room2",2)
    house2.add_room("room3",3)
    print(house.is_similar_house(house2))

    house2.add_room("room3",3)
    print(house.is_similar_house(house2))


if __name__ == "__main__":
    main()
