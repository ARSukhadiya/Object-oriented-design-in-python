from abc import ABC, abstractmethod
from typing import Optional
from enum import Enum

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer) -> None:
        pass

    @abstractmethod
    def removeObserver(self, observer) -> None:
        pass

    @abstractmethod
    def notifyObserver(self, house, event):
        pass


class EventType(Enum):
    HOUSE_ADDED = 1
    HOUSE_PRICE_UPDATED = 2
    HOUSE_SOLD = 3


class Displayable(ABC):
    @abstractmethod
    def display():
        pass


class House(Displayable):
    def __init__(self, address, squareFeet, numRooms, price):
        self.__address = address
        self.__squareFeet = squareFeet
        self.__numRooms = numRooms
        self.__price = price

    @property
    def address(self) -> str:
        return self.__address
    
    @property
    def price(self) -> str:
        return self.__price
    
    @price.setter
    def price(self, price) -> None:
        self.__price = price

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, House):
            return self.__address == __value.__address
        else:
            return False

    def __str__(self) -> str:
        return f"Address = {self.__address}, Square Feet = {self.__squareFeet}, Num of Rooms = {self.__numRooms}, Price = {self.__price}"

    def display(self):
        print(self)



class Observer(ABC):
    @abstractmethod
    def update(self, event: EventType) -> None:
        pass

    @abstractmethod
    def isRelatedToHouse(self, house: House, event: EventType) -> bool:
        pass


class Contact(Displayable):
    def __init__(self, firstName, lastName, phoneNumber, email):
        self.__lastName = lastName
        self.__firstName = firstName
        self.__email = email
        self.__phoneNumber = phoneNumber

    @property
    def lastName(self) -> str:
        return self.__lastName
    
    @property
    def firstName(self) -> str:
        return self.__firstName
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Contact):
            return self.__email == __value.__email
        else:
            return False

    def __str__(self) -> str:
        return f"Last Name = {self.__lastName}, First Name = {self.__firstName}, Phone Number = {self.__phoneNumber}, Email = {self.__email}"

    def display(self):
        print(self)


class Owner(Contact, Observer):
    def __init__(self, lastName: str, firstName: str, phoneNumber: str, email: str):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__houses: list[House] = []

    def __str__(self) -> str:
        output = super().__str__() + "\n"
        output += "Owns the following houses:"
        for house in self.__houses:
            output += "\n" + str(house)
        return output

    def addHouse(self, house: House) -> None:
        if house not in self.__houses:
            self.__houses.append(house)

    def update(self, event: EventType) -> None:
        if event == EventType.HOUSE_ADDED:
            print(f"{self.firstName} {self.lastName} has been notified that one of their houses has been added to the list.")
        elif event == EventType.HOUSE_PRICE_UPDATED:
            print(f"{self.firstName} {self.lastName} has been notified that one of their houses has its price updated.")
        elif event == EventType.HOUSE_SOLD:
            print(f"{self.firstName} {self.lastName} has been notified that one of their houses has been sold out.")

    def isRelatedToHouse(self, house: House, event: EventType) -> bool:
        return house in self.__houses

    def display(self) -> None:
        print(self)


class Buyer(Contact, Observer):
    def __init__(self, lastName: str, firstName: str, phoneNumber: str, email: str):
        super().__init__(lastName, firstName, phoneNumber, email)
        # self.__company = company
        self.__watchList = []
        # self.__company.registerObserver()

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

    def update(self, event: EventType) -> None:
        if event == EventType.HOUSE_ADDED:
            print(f"{self.firstName} {self.lastName}: a new house has been added.")
        elif event == EventType.HOUSE_PRICE_UPDATED:
            print(f"{self.firstName} {self.lastName}: one of your watched houses has its price updated.")
        elif event == EventType.HOUSE_SOLD:
            print(f"{self.firstName} {self.lastName} one of your watched houses has been sold out.")

    def isRelatedToHouse(self, house: House, event: EventType) -> bool:
        return house in self.__watchList or event == EventType.HOUSE_ADDED

    def display(self) -> None:
        print(self)


class Company(Subject, Displayable):
    def __init__(self, companyName: str):
        self.__companyName: str = companyName
        self.__owners: list[Owner] = []
        self.__buyers: list[Buyer] = []
        self.__agents: list[Agent] = []
        self.__houses: list[House] = []
        self.__observers: list[Observer] = []

    @property
    def houses(self) -> list:
        return self.__houses

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
    
    def registerObserver(self, observer: Observer) -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)

    def removeObserver(self, observer: Observer) -> None:
        i = self.__observers.index(observer)
        if i >= 0:
            self.__observers.pop(i)

    def notifyObserver(self, house: House, event: EventType) -> None:
        for observer in self.__observers:
            if observer.isRelatedToHouse(house, event):
                observer.update(event)

    def addOwner(self, owner: Owner) -> None:
        if owner not in self.__owners:
            self.__owners.append(owner)
        self.registerObserver(owner)

    def addBuyer(self, buyer: Buyer) -> None:
        if buyer not in self.__buyers:
            self.__buyers.append(buyer)
        self.registerObserver(buyer)
    
    def addAgent(self, agent) -> None:
        if agent not in self.__agents:
            self.__agents.append(agent)
        self.registerObserver(agent)

    def addHouseToListing(self, house: House) -> None:
        if house not in self.__houses:        
            self.__houses.append(house)
        self.notifyObserver(house, EventType.HOUSE_ADDED)

    def getHouseByAddress(self, address: str) -> Optional[House]:
        for house in self.__houses:
            if house.address == address:
                return house
        print("No house found with that address.")
        return None

    def removeHouseFromListing(self, house: House) -> None:
        try:
            i = self.__houses.index(house)
            self.__houses.pop(i)
            self.notifyObserver(house, EventType.HOUSE_SOLD)
            self.removeHouseFromSaveForLater(house)
            for observer in self.__observers:
                if observer.isRelatedToHouse(house, EventType.HOUSE_SOLD):
                    self.removeObserver(observer)
        except ValueError:
            print("Not found")


    # Help to remove that house from all buyers' watch list.
    def removeHouseFromSaveForLater(self, house: House):
        for buyer in self.__buyers:
            buyer.removeFromSaveForLater(house)        

    def getBuyersByHouse(self, house: House) -> list:
        return_list: list[Buyer] = []

        for buyer in self.__buyers:
            if house in buyer.watchList:
                return_list.append(buyer)
        
        return return_list

    def updatePrice(self, address: str, newPrice: float) -> None:
        house = self.getHouseByAddress(address)
        if house is not None:
            if newPrice != house.price:
                house.price = newPrice
                self.notifyObservers(house, EventType.HOUSE_PRICE_UPDATED)

    def display(self) -> None:
        print(self)


class Agent(Observer, Contact):
    def __init__(self, lastName: str, firstName: str, phoneNumber: str, email: str, position: str, company: Company):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__position: str = position
        self.__company: Company = company
        self.__company.registerObserver(self)

    def __str__(self) -> str:
        return super().__str__() + f"\nPosition = {self.__position}"

    def addHouseToListingForOwner(self, owner: Owner, house: House) -> None:
        self.__company.addOwner(owner)
        owner.addHouse(house)
        self.__company.addHouseToListing(house)

    def helpBuyerToSaveForLater(self, buyer: Buyer, house: House) -> None:
        buyer.saveForLater(house)
        self.__company.addBuyer(buyer)

    def editHousePrice(self, address: str, newPrice: int) -> None:
        house = self.__company.getHouseByAddress(address)
        if house is not None:
            house.price = newPrice

    def soldHouse(self, house: House) -> None:
        self.__company.removeHouseFromListing(house)
        self.__company.removeHouseFromSaveForLater(house)

    def editHousePrice(self, address: str, newPrice: int) -> None:
        house = self.__company.getHouseByAddress(address)
        if house is not None:
            house.price = newPrice

    # print all potential buyers who are interested in buying that house
    def printPotentalBuyers(self, house: House) -> None:
        for buyer in self.__company.getBuyersByHouse(house):
            buyer.display()

    def isRelatedToHouse(self, house: House, event:EventType) -> bool:
        return True
    
    def update(self, event: EventType) -> None:
        if event.HOUSE_ADDED:
            print(f"Agent:{self.firstName} A new house is added to the listing.")
        elif event.HOUSE_SOLD:
            print(f"Agent:{self.firstName} A house is sold.")
        elif event.HOUSE_PRICE_UPDATED:
            print(f"Agent:{self.firstName} A house price is updated.")

    def display(self) -> None:
        print(self)


def main():
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000)
    house2 = House('2222 Mission Blvd', 2000, 3, 1500000)
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000)

    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)
    company.addAgent(agent1)

    print("Adding Houses to the listing ..........................")
    agent1.addHouseToListingForOwner(owner1, house1)
    agent1.addHouseToListingForOwner(owner2, house2)
    agent1.addHouseToListingForOwner(owner2, house3)

    print('\nAdding buyers to the list ..........................')
    agent1.helpBuyerToSaveForLater(buyer1, house1)
    agent1.helpBuyerToSaveForLater(buyer1, house2)
    agent1.helpBuyerToSaveForLater(buyer1, house3)

    print('\nAdding buyers to the list ..........................')
    agent1.helpBuyerToSaveForLater(buyer2, house2)
    agent1.helpBuyerToSaveForLater(buyer2, house3)

    print('\nEditing house price ..........................')
    agent1.editHousePrice('2222 Mission Blvd', 1200000)

    print('\nDisplaying the company ..........................')
    company.display()

    print('\nAfter one house was sold ..........................')
    agent1.soldHouse(house3)
    company.display()

    print('\nDisplaying potential buyers for house 1 ..........................')
    agent1.printPotentalBuyers(house1)


if __name__ == "__main__":
    main()
