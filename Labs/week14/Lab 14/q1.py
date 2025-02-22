from __future__ import annotations
from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)

@acts_as_state_machine
class OrderProcess:
    # define states
    checkout = State(initial=True)
    selectFlavor = State()
    placedOrder = State()
    preparingOrder = State()
    makingOrder = State()
    ReadyForPickupOrder = State()
    CompletedOrder = State()

    # Define transictions
    select_flavor = Event(from_states=checkout, to_state=selectFlavor)
    check_inventory = Event(from_states=selectFlavor, to_state=placedOrder)
    prepare_order = Event(from_states=placedOrder, to_state=preparingOrder)
    cancel_order = Event(from_states=(selectFlavor, placedOrder), to_state=checkout)
    
    making_ice_cream = Event(from_states=preparingOrder, to_state=makingOrder)
    finishing_ice_cream = Event(makingOrder=selectFlavor, to_state=ReadyForPickupOrder)
    pickup_order = Event(from_states=ReadyForPickupOrder, to_state=CompletedOrder)
    ready_to_order = Event(from_states=CompletedOrder, to_state=checkout)

    def __init__(self, store: IceCreamStore) -> None:
        self.store = store

    @before('check_inventory')
    def before_check_inventory(self):
        total_lbs = self.store.selected_quantity  * self.store.sizes[self.store.selected_size]
        if total_lbs >= self.store.inventory[self.store.selected_flavor]:
            return False
        else:
            return True
        
    @after('ready_to_order')
    def after_ready_to_order(self):
        print(f"The ")

    # @before('select_flavor')
    # def before_select_flavor(self):
        

class IceCreamStore:
    def __init__(self) -> None:
        self.process = OrderProcess(self)
        self.inventory = {"Vanilla": 5, "Chocolate": 2, "Strawberry": 1}
        self.sizes = {"large": 1, "medium": 0.5, "small": 0.25}
        self.selected_flavor = None
        self.selected_size = None
        self.selected_quantity = None

    def select_flavor(self, flavor, size, quantity):
        self.selected_flavor = flavor
        self.selected_size = size
        self.selected_quantity = quantity
        self.process.select_flavor()

    def check_inventory(self):
        self.process.check_inventory()

    def prepare_order(self):
        self.process.prepare_order()

    def cancel_order(self):
        self.process.cancel_order()

    def making_ice_cream(self):
        self.process.making_ice_cream()

    def finishing_ice_cream(self):
        self.process.finishing_ice_cream()

    def pickup_order(self):
        self.process.making_ice_cream()

    def ready_to_order(self):
        self.process.ready_to_order()

    def get_current_process(self):
        return self.process.current_state



def show_menu():
    print("===MENU===")
    print("1. Select flavor")
    print("2. Check Inventory")
    print("3. Prepare Order")
    print("4. Make Order")
    print("5. Finish Order")
    print("6. Pickup Order")
    print("7. Cancel Order")
    print("8. Ready for next customer")
    print("9. Exit")


def main():
    store = IceCreamStore()
    
    while True:
        show_menu()
        try:
            option = int(input("Enter your option: "))
            if option == 1:
                flavor = input("Enter flavor(Vanilla, Chocolate, Strawberry): ")
                size = input("Enter size(large, medium, small): ")
                quantity = int(input("Enter quantity: "))
                store.select_flavor(flavor, size, quantity)

            elif option == 2:
                store.check_inventory()
            elif option == 3:
                store.prepare_order()
            elif option == 4:
                store.making_ice_cream()
            elif option == 5:
                store.finishing_ice_cream()
            elif option == 6:
                store.pickup_order()
            elif option == 7:
                store.cancel_order()
            elif option == 8:
                store.prepare_order()
            else:
                break
            print(f"Now is in {store.get_current_process()} state")
        except ValueError as ex:
            print(f"Could not perform option {option} in {store.get_current_process()}")


if __name__ == "__main__":
    main()
