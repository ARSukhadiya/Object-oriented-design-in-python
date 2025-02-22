from __future__ import annotations

from abc import ABC, abstractmethod

class LightState(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def turn_on(self, light_switch):
        raise ValueError(f"Cannot turn on in {self.name} state")
    
    def turn_off(self, light_switch):
        raise ValueError(f"Cannot turn off in {self.name} state")
    
    def dim(self, light_switch):
        raise ValueError(f"Cannot dim in {self.name} state")
    

class OffState(LightState):
    def __init__(self) -> None:
        super().__init__('OFF')

    def turn_on(self, light_switch):
        light_switch.state = OnState()
        print("Light is on now")


class OnState(LightState):
    def __init__(self) -> None:
        super().__init__('ON')

    def turn_off(self, light_switch):
        light_switch.state = OffState()
        print("Light is off now")
    
    def dim(self, light_switch):
        light_switch.state = DimState()
        print("Light is dimmed now")


class DimState(LightState):
    def __init__(self) -> None:
        super().__init__('DIM')

    def turn_off(self, light_switch):
        light_switch.state = OffState()
        print("Light is off now")
    
    def turn_on(self, light_switch):
        light_switch.state = OnState()
        print("Light is on now")


class LightSwitch:
    def __init__(self) -> None:
        self.state: LightState = OffState()

    def turn_on(self):
        self.state.turn_on(self)

    def turn_off(self):
        self.state.turn_off(self)

    def dim(self):
        self.state.dim(self)


def show_menu():
    print("===MENU===")
    print("1. Turn on")
    print("2. Turn off")
    print("3. Dim")
    print("4. Exit")


def main():
    switch = LightSwitch()
    # switch.turn_off()
    while True:
        show_menu()
        try:
            option = int(input("Enter your option: "))
            if option == 1:
                switch.turn_on()
            elif option == 2:
                switch.turn_off()
            elif option == 3:
                switch.dim()
            else:
                break
        except ValueError as ex:
            print(ex)


if __name__ == "__main__":
    main()
