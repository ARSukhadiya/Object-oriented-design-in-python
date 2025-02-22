from vehicle import Vehicle, Truck, SUV, Sedan, Minivan
import csv

class VehicleRepository:
    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def save_vehicles(self, vehicles: list[Vehicle]):
        with open(self.__filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for vehicle in vehicles:
                writer.writerow(vehicle.convert_to_list())

    def read_vehicles(self) -> list[Vehicle]:
        vehicles: list[Vehicle] = []
        with open(self.__filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                vehicle = Vehicle(row[0], row[1], row[2], row[3])
                vehicles.append(vehicle)
        return vehicles
    

def main():
    truck1 = Truck("TRK2010.1", "LIGHT GREY", 2010, "Short Bed")
    suv1 = SUV("SUV2011.1B", "LIGHT BROWN", 2011, "Standard")
    sedan1 = Sedan("SDN2000_W", "LOW WHITE", 2000)
    minivan1 = Minivan("MNV2005_B", "SHINE WHITE", 2005)

    vehicles: list[Vehicle] = []
    vehicles.append(truck1)
    vehicles.append(suv1)
    vehicles.append(sedan1)
    vehicles.append(minivan1)

    repos = VehicleRepository("vehicles.csv")
    repos.save_vehicles(vehicles)

    vehicles2 = repos.read_vehicles()
    for vehicle in vehicles2:
        print(vehicle)


if __name__ == "__main__":
    main()
