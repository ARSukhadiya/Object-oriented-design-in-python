from abc import ABC, abstractmethod
import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)

    def execute(self, query, params=None):
        if params is None:
            params = []

        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor.fetchall()
    
###########################################################
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CreateTableCommand(Command):
    def __init__(self, database: Database, table_name: str, columns: dict[str, str]) -> None:
        self.__database = database
        self.__table_name = table_name
        self.__columns = columns

    def execute(self):
        query = "CREATE TABLE IF NOT EXISTS " + self.__table_name + "("
        for column, data_type in self.__columns.items():
            query += column + " " + data_type + ", "
        query = query[:-2] + ")"        
        self.__database.execute(query)


class InsertCommand(Command):
    def __init__(self, database: Database, table_name: str, values: list) -> None:
        self.__database: Database = database
        self.__table_name: str = table_name
        self.__values: list = values

    def execute(self):
        query = "INSERT INTO " + self.__table_name + " VALUES ("
        for element in self.__values:
            query += str(element) + ", "
        query = query[:-2] + ")"
        self.__database.execute(query)
    

class SelectCommand(Command):
    def __init__(self, database: Database, table_name: str, where: str = None) -> None:
        self.__database = database
        self.__table_name = table_name
        self.__where = where

    def execute(self):
        query = "SELECT * FROM " + self.__table_name 
        if self.__where:
            query += " WHERE " + self.__where
        
        # print('query:', query)
        return self.__database.execute(query)


class UpdateCommand(Command):
    def __init__(self, database, table_name: str, col_value: str, where: str = None) -> None:
        self.__database = database
        self.__table_name = table_name
        self.__where = where
        self.__col_value = col_value

    def execute(self):
        query = "UPDATE " + self.__table_name + " SET " + self.__col_value
        if self.__where:
            query += " WHERE " + self.__where
        
        # print('query:', query)
        return self.__database.execute(query)


class DeleteCommand(Command):
    def __init__(self, database, table_name: str, where: str = None) -> None:
        self.__database = database
        self.__table_name = table_name
        self.__where = where

    def execute(self):
        query = "DELETE FROM " + self.__table_name
        if self.__where:
            query += " WHERE " + self.__where
        
        # print('query:', query)
        return self.__database.execute(query)


class Invoker:
    def __init__(self) -> None:
        self.__createTableCommand: CreateTableCommand = None
        self.__insertCommands: list[InsertCommand] = []
        self.__updateCommand: UpdateCommand = None
        self.__deleteCommand: DeleteCommand = None
        self.__selectCommand: SelectCommand = None

    def set_command(self, command: Command):
        if isinstance(command, CreateTableCommand):
            self.__createTableCommand = command
        if isinstance(command, InsertCommand):
            self.__insertCommands.append(command)
        if isinstance(command, UpdateCommand):
            self.__updateCommand = command
        if isinstance(command, DeleteCommand):
            self.__deleteCommand = command
        if isinstance(command, SelectCommand):
            self.__selectCommand = command

    def createTable(self):
        self.__createTableCommand.execute()

    def insertRecord(self):
        for command in self.__insertCommands:
            command.execute()

    def updateRecord(self):
        self.__updateCommand.execute()

    def deleteRecord(self):
        self.__deleteCommand.execute()

    def selectRecord(self):
        return self.__selectCommand.execute()


def main():
    database  = Database("test.db")
    table = "users"
    columns = ["id", "name"]
    invoker = Invoker()

    def print_table(selected_data = None):
        print("\nTable:", table)
        print("-"*13)
        
        if selected_data == None:
            print("No record found!")
            return False
        
        print(f"{columns[0]:3} | {columns[1]:10}\n" + "-"*13)
        for data in selected_data:
            print(f"{data[0]:3} | {data[1]:10}")

    invoker.set_command(CreateTableCommand(database, table, {columns[0]: "INTEGER PRIMARY KEY", columns[1]: "TEXT"}))
    
    invoker.set_command(InsertCommand(database, table, [101, "'Bob'"]))
    invoker.set_command(InsertCommand(database, table, [102, "'Steve'"]))
    invoker.set_command(InsertCommand(database, table, [103, "'Gerry'"]))
    invoker.set_command(InsertCommand(database, table, [104, "'Tom'"]))
    
    invoker.set_command(SelectCommand(database, table))

    invoker.set_command(UpdateCommand(database, table, col_value="name='Boby'", where="id = 101"))

    invoker.set_command(DeleteCommand(database, table, where="id = 104"))

    print("\nCreating table...")
    invoker.createTable()

    print("\nInserting records...")
    invoker.insertRecord()
    print_table(invoker.selectRecord())

    print("\nUpdating data of the table...")
    invoker.updateRecord()
    print_table(invoker.selectRecord())

    print("\nDeleting data of the table...")
    invoker.deleteRecord()
    print_table(invoker.selectRecord())


if __name__ == "__main__":
    main()
