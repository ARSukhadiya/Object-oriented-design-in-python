from abc import ABC, abstractmethod
from typing import Optional


class Displayable(ABC):
    @abstractmethod
    def display() -> None:
        pass


class House(Displayable):
    def __init__(self, address: str, squareFeet: int, numRooms: int, price: int):
        self.__address: str = address
        self.__squareFeet: int = squareFeet
        self.__numRooms: int = numRooms
        self.__price: int = price

    # add some public properties here if necessary 
    @property
    def address(self) -> str:
        return self.__address
    
    @property
    def price(self) -> str:
        return self.__price
    
    @price.setter
    def price(self, price: int) -> None:
        self.__price = price

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, House):
            return self.__address == __value.__address
        else:
            return False

    def __str__(self) -> str:
        return f"Address = {self.__address}, Square Feet = {self.__squareFeet}, Num of Rooms = {self.__numRooms}, Price = {self.__price}"

    def display(self) -> None:
        print(self)


class Contact(Displayable):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, email: str):
        self.__lastName: str = lastName
        self.__firstName: str = firstName
        self.__email: str = email
        self.__phoneNumber: str = phoneNumber

    # add some public properties here if necessary 

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Contact):
            return self.__email == __value.__email
        else:
            return False

    def __str__(self) -> str:
        return f"Last Name = {self.__lastName}, First Name = {self.__firstName}, Phone Number = {self.__phoneNumber}, Email = {self.__email}"

    def display(self) -> None:
        print(self)


class Owner(Contact):
    def __init__(self, lastName: str, firstName: str, phoneNumber: str, email: str):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__houses: list[House] = []

    def __str__(self) -> str:
        output = super().__str__() + "\n"
        output += "Owns the following houses:"
        for house in self.__houses:
            output += "\n" + str(house)
        return output

    def addHouse(self, house) -> None:
        self.__houses.append(house)

    def display(self) -> None:
        print(self)

class Buyer(Contact):
    def __init__(self, lastName: str, firstName: str, phoneNumber: str, email: str):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__watchList: list[House] = []

    @property
    def watchList(self) -> list:
        return self.__watchList
    
    def __str__(self) -> str:
        output = super().__str__() + "\n"
        output += "Watching the following houses:"
        for house in self.__watchList:
            output += "\n" + str(house)
        return output

    #  Save the house in his watch list 
    def saveForLater(self, house: House) -> None:
        if house not in self.__watchList:
            self.__watchList.append(house)

    # Remove the house from his watch list
    def removeFromSaveForLater(self, house: House) -> None:
        try:
            i = self.__watchList.index(house)
            self.__watchList.pop(i)
        except ValueError:
            print("Not found")

    def display(self) -> None:
        print(self)


class Company(Displayable):
    def __init__(self, companyName: str):
        self.__companyName: str = companyName
        self.__owners: list[Owner] = []
        self.__buyers: list[Buyer] = []
        self.__agents: list[Agent] = []
        self.__houses: list[House] = []

    def __str__(self) -> str:
        output = "Company Name = " + self.__companyName 
        output += "\n=========================== The list of agents: =============================="
        for agent in self.__agents:
            output += "\n" + str(agent)

        output += "\n=========================== The house listing: =============================="
        for house in self.__houses:
            output += "\n" + str(house)
    
        output += "\n=========================== The list of owners: =============================="
        for owner in self.__owners:
            output += "\n" + str(owner)
    
        output += "\n=========================== The list of buyers: =============================="
        for buyer in self.__buyers:
            output += "\n" + str(buyer)
        
        return output
    
    def addOwner(self, owner) -> None:
        if owner not in self.__owners:
            self.__owners.append(owner)

    def addBuyer(self, buyer) -> None:
        if buyer not in self.__buyers:
            self.__buyers.append(buyer)

    def addAgent(self, agent) -> None:
        if agent not in self.__agents:
            self.__agents.append(agent)

    def addHouseToListing(self, house: House) -> None:
        if house not in self.__houses:        
            self.__houses.append(house)

    def getHouseByAddress(self, address: str) -> Optional[House]:
        for house in self.__houses:
            if house.address == address:
                return house
        return None

    def removeHouseFromListing(self, house: House) -> None:
        try:
            i = self.__houses.index(house)
            self.__houses.pop(i)
            self.removeHouseFromSaveForLater(house)
        except ValueError:
            print("Not found")

    # Help to remove that house from all buyers' watch list.
    def removeHouseFromSaveForLater(self, house: House) -> None:
        for buyer in self.__buyers:
            buyer.removeFromSaveForLater(house)

    def getBuyersByHouse(self, house: House) -> str:
        output = ""
        for buyer in self.__buyers:
            if house in buyer.watchList:
                output += str(buyer)
        
        return output

    def display(self) -> None:
        print(self)

class Agent(Contact):
    def __init__(self, lastName: str, firstName: str, phoneNumber: str, email: str, position: str, company: Company):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__position: str = position
        self.__company: Company = company

    def __str__(self) -> str:
        return super().__str__() + f"\nPosition = {self.__position}"

    def addHouseToListingForOwner(self, owner: Owner, house: House) -> None:
        self.__company.addOwner(owner)
        self.__company.addHouseToListing(house)

    def helpBuyerToSaveForLater(self, buyer: Buyer, house: House) -> None:
        buyer.saveForLater(house)
        self.__company.addBuyer(buyer)

    def editHousePrice(self, address: str, newPrice: int) -> None:
        house = self.__company.getHouseByAddress(address)
        if house is not None:
            house.price = newPrice

    def soldHouse(self, house:House) -> None:
        self.__company.removeHouseFromListing(house)

    # print all potential buyers who are interested in buying that house
    def printPotentalBuyers(self, house: House) -> None:
        print(self.__company.getBuyersByHouse(house))

    def display(self) -> None:
        print(self)


def main():
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000)
    house2 = House('2222 Mission Blvd', 2000, 3, 1500000)
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000)

    owner1.addHouse(house1)
    owner2.addHouse(house2)
    owner2.addHouse(house3)

    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)
    company.addAgent(agent1)

    agent1.addHouseToListingForOwner(owner1, house1)
    agent1.addHouseToListingForOwner(owner2, house2)
    agent1.addHouseToListingForOwner(owner2, house3)

    agent1.helpBuyerToSaveForLater(buyer1, house1)
    agent1.helpBuyerToSaveForLater(buyer1, house2)
    agent1.helpBuyerToSaveForLater(buyer1, house3)

    agent1.helpBuyerToSaveForLater(buyer2, house2)
    agent1.helpBuyerToSaveForLater(buyer2, house3)

    agent1.editHousePrice('2222 Mission Blvd', 1200000)

    company.display()

    print('\nAfter one house was sold ..........................')
    agent1.soldHouse(house3)
    company.display()

    print('\nDisplaying potential buyers for house 1 ..........................')
    agent1.printPotentalBuyers(house1)



if __name__ == "__main__":
    main()
