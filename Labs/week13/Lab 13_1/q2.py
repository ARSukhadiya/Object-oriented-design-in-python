from abc import ABC, abstractmethod

class Database:
    def insert(self):
        print("Record inserted.")

    def update(self):
        print("Record updated.")

    def delete(self):
        print("Record deleted.")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class InsertCommand(Command):
    def __init__(self, database: Database) -> None:
        self.__database = database

    def execute(self):
        self.__database.insert()


class UpdateCommand(Command):
    def __init__(self, database: Database) -> None:
        self.__database = database

    def execute(self):
        self.__database.update()

class DeleteCommand(Command):
    def __init__(self, database: Database) -> None:
        self.__database = database

    def execute(self):
        self.__database.delete()

class Client:
    def __init__(self) -> None:
        self.__commands: list[Command] = []

    def set_command(self, command: Command):
        self.__commands.append(command)

    def execute_command(self, command_no: int):
        self.__commands[command_no].execute()

    def execute_all(self):
        for command in self.__commands:
            command.execute()

    def undo_all(self):
        for command in reversed(self.__commands):
            command.execute()        


def main():
    db = Database()
    client = Client()
    client.set_command(InsertCommand(db))
    client.set_command(UpdateCommand(db))
    client.set_command(DeleteCommand(db))

    client.execute_command(1)
    client.execute_all()
    client.undo_all()

if __name__ == "__main__":
    main()