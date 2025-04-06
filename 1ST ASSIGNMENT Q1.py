class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        return "Engine starting... (Generic vehicle sound)"


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    # Overriding the start_engine method
    def start_engine(self):
        return "Vroom! Car engine started."

    # Adding a car-specific method
    def honk(self):
        return "Beep beep!"


class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    # Overriding the start_engine method
    def start_engine(self):
        if self.bike_type == "electric":
            return "Whirrr... Electric bike powered on."
        else:
            return "Pedaling... (No engine on this bike)"


# Demonstration
if __name__ == "__main__":
    # Create instances
    generic_vehicle = Vehicle("Generic", "Transport", 2020)
    my_car = Car("Toyota", "Camry", 2022, 4)
    my_bike = Bike("Trek", "FX", 2023, "regular")
    e_bike = Bike("Rad", "Power", 2023, "electric")

    # Test the methods
    print(generic_vehicle.start_engine())  # Base class implementation
    print(my_car.start_engine())  # Car's overridden method
    print(my_bike.start_engine())  # Bike's overridden method
    print(e_bike.start_engine())  # Bike's overridden method with condition

    # Display info (inherited from Vehicle)
    print("\nVehicle information:")
    print(my_car.display_info())
    print(my_bike.display_info())