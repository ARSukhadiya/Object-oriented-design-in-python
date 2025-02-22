from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)


@acts_as_state_machine
class LightProcess:
    # Define states
    off = State(initial=True)
    on = State()
    dim = State()

    # Define transitions (events)
    turn_on = Event(from_states=(on, off), to_state=on)
    turn_off = Event(from_states=(on, dim), to_state=off)
    dimming = Event(from_states=on, to_state=dim)

    @before('turn_on')
    def before_turn_on(self):
        confirm = input("Are you sure to turn on the light? ")
        return True if confirm.lower() == 'yes' else False

    @after('turn_on')
    def after_turn_on(self):
        print("You have turned on the Light.")


class LightSwitch:
    def __init__(self) -> None:
        self.state = LightProcess()

    def turn_on(self):
        self.state.turn_on()

    def turn_off(self):
        self.state.turn_off()

    def dim(self):
        self.state.dimming()

    def get_current_state(self):
        return self.state.current_state


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
            print(f"Now is in {switch.get_current_state()} state")
        except InvalidStateTransition as e:
            print(f"Could not perform option {option} in {switch.get_current_state()}")


if __name__ == "__main__":
    main()
