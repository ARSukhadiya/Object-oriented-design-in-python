from vehicle import Vehicle
from vehicle_repos import VehicleRepository
# from order_repos import OrderRepository

class DealerInventory:
    def __init__(self) -> None:
        self.__vehicles: list[Vehicle] = []
        self.__orders = []

    def __str__(self) -> str:
        output = f"Dealer_Name: {self.__name}, Address: {self.__address}"
        return output

    def add_vehicle(self, vehicle: Vehicle) -> None:
        try:
            self.__vehicles.append(vehicle)

            # save latest vehicle data to DB
            self.save_vehicles_to_db()
            print("\nVehicle inserted successfully!")
        
        except Exception as exc:
            print("\n!Vehicle could not be Inserted")
            print("Exception:\n", exc)

    def display_vehicles(self) -> None:
        for vehicle in self.__vehicles:
            print(vehicle)

    def search_vehicle(self, model) -> list[Vehicle]:
        found_vehicles = []
        for vehicle in self.__vehicles:
            if vehicle._model == model:
                found_vehicles.append(vehicle)
        
        return found_vehicles

    def get_vehicle(self, model, model_yr) -> Vehicle:
        for vehicle in self.__vehicles:
            if vehicle._model == model and vehicle._model_yr == model_yr:
                found_vehicle = vehicle
        
        return found_vehicle

    def update_vehicle(self, model, base_price = None, model_yr = None) -> bool:
        vehicle_updated = False
        for vehicle in self.__vehicles:
            if vehicle._model == model:
                if base_price:
                    vehicle._base_price = base_price
                    vehicle_updated = True
                elif model_yr:
                    vehicle._model_yr = model_yr
                    vehicle_updated = True
        
        if vehicle_updated:
            # save latest customer data to DB
            self.save_vehicles_to_db()
            print('Record updated successfully!')

        return vehicle_updated

    def remove_vehicle(self, model) -> bool:
        vehicle_deleted = False
        for i in range(len(self.__vehicles)):
            if self.__vehicles[i]._model == model:
                self.__vehicles.pop(i)
                vehicle_deleted = True

        if vehicle_deleted:
            # save latest customer data to DB
            self.save_vehicles_to_db()
            print('Record deleted successfully!')

        return vehicle_deleted

    def get_most_expensive_vehicle(self) -> Vehicle:
        expensive_vehicle = None
        price = 0
        for vehicle in self.__vehicles:
            if int(vehicle._base_price) > price:
                price = int(vehicle._base_price)
                expensive_vehicle = vehicle
        
        return expensive_vehicle

    def get_least_expensive_vehicle(self) -> Vehicle:
        lease_expensive_vehicle = None
        price = 0
        for i in range(len(self.__vehicles)):
            if i == 1:
                price = int(self.__vehicles[i]._base_price)
                lease_expensive_vehicle = self.__vehicles[i]

            if int(self.__vehicles[i]._base_price) < price:
                price = int(self.__vehicles[i]._base_price)
                lease_expensive_vehicle = self.__vehicles[i]
        
        return lease_expensive_vehicle

    def add_customized_order(self, c_id, c_name, model, model_yr, color, features, base_price, additional_charge) -> int:
        try:
            self.__orders.append([c_id, c_name, model, model_yr, color, features, base_price, additional_charge])
            
            # save latest order data to DB
            self.save_orders_to_db()
            print("\nOrder inserted successfully!")
        
        except Exception as exc:
            print("\n!Order could not be Inserted")
            print("Exception:\n", exc)

        return base_price + additional_charge


    def get_vehicles_from_db(self):
        repos = VehicleRepository('vehicles.csv')
        self.__vehicles = repos.read_vehicles()

    def save_vehicles_to_db(self):
        repos = VehicleRepository("vehicles.csv")
        repos.save_vehicles(self.__vehicles) 

    # def get_orders_from_db(self):
    #     repos = OrderRepository('orders.csv')
    #     self.__orders = repos.read_orders()

    # def save_orders_to_db(self):
    #     repos = OrderRepository("orders.csv")
    #     repos.save_orders(self.__orders) 


def main():
    dealer = DealerInventory()

    cont = True
    while cont is True:
        dealer.show_menu()
        cont = dealer.process_command(int(input("Enter your choice: ")))
        

if __name__ == "__main__":
    main()
