from abc import ABC, abstractmethod

# Receiver
class Washer:
    def wash(self, temp: int, cycles: int):
        print(f"Washing with {temp = } and {cycles = }")


class TV:
    def watch(self, channel: int):
        print(f"Watching {channel = }")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class WashCommand(Command):
    def __init__(self, temp: int, cycles: int, washer: Washer) -> None:
        self.__obj = washer
        self.__temp = temp
        self.__cycles = cycles

    def execute(self):
        self.__obj.wash(self.__temp, self.__cycles)


class WatchCommand(Command):
    def __init__(self, channel: int, tv: TV) -> None:
        self.__obj = tv
        self.__channel = channel

    def execute(self):
        self.__obj.watch(self.__channel)


class Invoker:                      # Remote Control
    def __init__(self) -> None:
        self.__buttons: list[Command] = []

    def add_command(self, command: Command):
        self.__buttons.append(command)

    def execute_command(self, button_no: int):
        self.__buttons[button_no].execute()

    def execute_all(self):
        for button in self.__buttons:
            button.execute()
        

def main():
    washer = Washer()
    tv = TV()
    control = Invoker()
    control.add_command(WashCommand(80, 2, washer))
    control.add_command(WatchCommand(5, tv))

    control.execute_command(0)
    control.execute_command(1)

    control.execute_all()


if __name__ == "__main__":
    main()
