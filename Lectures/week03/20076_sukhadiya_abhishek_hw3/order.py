from dealer_inventory import DealerInventory
from vehicle import Vehicle, Sedan, Truck, SUV, Minivan, FeatureType


class Order(DealerInventory):
    def __init__(self, customer_name: str, customer_id: int) -> None:
        self.__inventory = DealerInventory()
        self.__inventory.get_vehicles_from_db()
        # self.__inventory.get_orders_from_db()
        self.__customer_name = customer_name
        self.__customer_id = customer_id
        self.__cart: list[Vehicle] = []
        self.__total_price = 0

    def __str__(self) -> str:
        output = f"Customer_id: {self.__customer_id}, Customer_name: {self.__customer_name} "
        if self.__cart:
            output += f"Cart: {self.__cart}"
        return output

    def show_menu(self):
        print("\n===== INVENTORY MENU ====")
        print("1. Add vehicle")
        print("2. View all vehicles")
        print("3. Search vehicle/s")
        print("4. Edit Vehicle details")
        print("5. Remove/Delete vehicle from inventory")
        print("6. Most expensive vehicle")
        print("7. Least expensive vehicle")
        print("\n===== ORDER MENU ====")
        print("8. Customize vehicle")
        print("10. Exit")

    def select_vehicle(self):
        vehicle: Vehicle = None

        try:
            print("Please enter the vehicle details:")
            model = input("Enter model: ")
            color = input("Enter color: ")
            model_yr = int(input("Enter model-year: "))

            print("""Available vehicles:
                1 - Sedan
                2 - Truck
                3 - SUV
                4 - Minivan
                """)
            
            while True:
                vehicle_type = int(input("Enter vehicle type(1/2/3/4): "))
                if vehicle_type == 1:
                    # Sedan
                    vehicle = Sedan(model, color, model_yr)
                    
                elif vehicle_type == 2:
                    # Truck
                    cargo_bed_size = input("Enter cargo bed_size(Short Bed, Long Bed): ")
                    vehicle = Truck(model, color, model_yr, cargo_bed_size)

                elif vehicle_type == 3:
                    # SUV
                    roof_rack_type = input("Enter roof-rack type (Standard, Heavy Duty): ")
                    vehicle = SUV(model, color, model_yr, roof_rack_type)

                elif vehicle_type == 4:
                    # Minivan
                    vehicle = Minivan(model, color, model_yr)
                
                else:
                    print("Invalid input!")
                    continue

                break   
        except ValueError as exc:
            print("!Input Value is invalid!")
            print("Exception:" , exc)

        return vehicle

    def select_feature(self) -> list:
        features: list[FeatureType] = []
        additional_charge = 0

        print("Enter 1/0 for select/disselect below Optional-Features: ")

        while True: 
            try:
                if int(input("Enhanced Safely: ")):
                    features.append(FeatureType.ENHANCED_SAFETY)
                    additional_charge += FeatureType.ENHANCED_SAFETY.value
                if int(input("Security: ")):
                    features.append(FeatureType.SECURITY)
                    additional_charge += FeatureType.SECURITY.value
                if int(input("Entertainment System: ")):
                    features.append(FeatureType.ENTERTAINMENT_SYSTEM)
                    additional_charge += FeatureType.ENTERTAINMENT_SYSTEM.value
                if int(input("Sunroof: ")):
                    features.append(FeatureType.SUNROOF)
                    additional_charge += FeatureType.SUNROOF.value
                
                break
            except ValueError as exc:
                print("!Input Value is invalid!")
                print("Exception:" , exc)
        
        return features, additional_charge


    def process_command(self, command) -> bool:
        cont = True

        if command == 1:
            # Add vehicle
            self.__inventory.add_vehicle(self.select_vehicle())

        elif command == 2:
            # View all vehicles
            self.__inventory.display_vehicles()

        elif command == 3:
            # Search vehicle/s
            model = input("Enter the model to search: ")
            searched_vehicles = self.__inventory.search_vehicle(model)
            if not searched_vehicles:
                print("Vehicle not found!")
            else:
                for vehicle in searched_vehicles:
                    print(vehicle)

        elif command == 4:
            # Edit Vehicle details
            model = input("Enter the model to edit details for: ")
            while True:
                base_price = input("Enter base_price (if you want to update): ")
                model_yr = input("Enter model year (if you want to update): ")
                if base_price or model_yr:
                    break

            if not self.__inventory.update_vehicle(model, base_price, model_yr):
                print("Vehicle detail couldn't be updated!")

        elif command == 5:
            # Remove/Delete vehicle from inventory
            model = input("Enter the model to delete: ")
            if not self.__inventory.remove_vehicle(model):
                print("Vehicle detail couldn't be removed!")

        elif command == 6:
            # Most expensive vehicle
            print(self.__inventory.get_most_expensive_vehicle())

        elif command == 7:
            # Least expensive vehicle
            print(self.__inventory.get_least_expensive_vehicle())

        elif command == 8:
            # Customize vehicle
            model = input("Enter the model: ")
            model_yr = input("Enter the model_yr: ")
            selected_vehicle = self.__inventory.get_vehicle(model, model_yr)
            print("Selected vehicle:\n    ", selected_vehicle)
            color = input("Enter color(if you want to update): ") or selected_vehicle._color
            features, additional_charge = self.select_feature()

            self.__total_price = self.__inventory.add_customized_order(self.__customer_id, self.__customer_name, model, model_yr, color, features, selected_vehicle._base_price, additional_charge)
            print("Total Price: ", self.__total_price)

        elif command == 10:
            # Exit
            cont = False

        return cont
    
    def display(self):
        print(self)

    def convert_to_list(self) -> list[str]:
        lst = []
        lst.append(self.__customer_name)
        lst.append(self.__customer_id)
        lst.append(self.__cart)
        return lst


def main():
    order = Order(customer_id=1001, customer_name="Stephen")


    cont = True
    while cont is True:
        order.show_menu()
        cont = order.process_command(int(input("Enter your choice: ")))
        

if __name__ == "__main__":
    main()
