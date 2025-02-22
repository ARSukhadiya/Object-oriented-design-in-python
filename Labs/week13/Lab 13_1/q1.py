from abc import ABC, abstractmethod

# abstract classes
class Light:
    def on(self):
        print("Light is on now.")

    def off(self):
        print("Light is off now.")


class Fan:
    def start(self):
        print("Fan is started now.")

    def stop(self):
        print("Fan is stopped now.")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Define command classes 
class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self.__light = light

    def execute(self):
        self.__light.on()


class LightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self.__light = light

    def execute(self):
        self.__light.off()


class FanStartCommand(Command):
    def __init__(self, fan: Fan) -> None:
        self.__fan = fan

    def execute(self):
        self.__fan.start()


class FanStopCommand(Command):
    def __init__(self, fan: Fan) -> None:
        self.__fan = fan

    def execute(self):
        self.__fan.stop()


class Control:
    def __init__(self) -> None:
        # self.__commands: list[Command] = []
        self.__lightOnCommand: LightOnCommand = None
        self.__lightOffCommand: LightOffCommand = None
        self.__fanStartCommand: FanStartCommand = None
        self.__fanStopCommand: FanStopCommand = None

    def set_command(self, command: Command):
        if type(command) == LightOnCommand:
            self.__lightOnCommand = command
        elif type(command) == LightOffCommand:
            self.__lightOffCommand = command
        if type(command) == FanStartCommand:
            self.__fanStartCommand = command
        if type(command) == FanStopCommand:
            self.__fanStopCommand = command

    def lightOnButtonPressed(self):
        self.__lightOnCommand.execute()

    def lightOffButtonPressed(self):
        self.__lightOffCommand.execute()

    def fanStartButtonPressed(self):
        self.__fanStartCommand.execute()

    def fanStopButtonPressed(self):
        self.__fanStopCommand.execute()


def main():
    light = Light()
    fan = Fan()
    control = Control()

    control.set_command(LightOnCommand(light))
    control.set_command(LightOffCommand(light))
    control.set_command(FanStartCommand(fan))
    control.set_command(FanStopCommand(fan))

    control.lightOnButtonPressed()
    control.lightOffButtonPressed()

    control.fanStartButtonPressed()
    control.fanStopButtonPressed()


if __name__ == "__main__":
    main()
