import sqlite3 
import datetime
from abc import ABC, abstractmethod
 
class QueryTemplate(ABC):
    def connect(self):
        self.conn = sqlite3.connect("sales.db")

    @abstractmethod
    def construct_query(self):
        pass

    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(", ".join(row))
        self.formatted_results = "\n".join(output)

    @abstractmethod
    def output_results(self):
        pass

    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()
        
class NewVehiclesQuery(QueryTemplate):
    def construct_query(self):
        self.query = "select * from Sales where new='true'"

    def output_results(self):
        print(self.formatted_results)


class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = (
            "select salesperson, sum(amt) "
            + " from Sales group by salesperson"
        )

    def output_results(self):
        filename = "gross_sales_{0}".format(
            datetime.date.today().strftime("%Y%m%d")
        )
        with open(filename, "w") as outfile:
            outfile.write(self.formatted_results)
            
            
def main():
    newVehicle = NewVehiclesQuery()
    newVehicle.process_format()
    
    print()
    userSales = UserGrossQuery()
    userSales.process_format()
    
if __name__ == "__main__":
    main()
    
    
    