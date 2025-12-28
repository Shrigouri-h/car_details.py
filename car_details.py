class Car:
    def __init__(self):
        self.brand = ""
        self.model = ""
        self.distance = 0.0  # in km
        self.time = 0.0      # in hours
        self.fuel = 0.0     # in liters

    def input_details(self):
        self.brand = input("Enter car brand: ")
        self.model = input("Enter car model: ")
        self.distance = float(input("Enter distance travelled (km): "))
        self.time = float(input("Enter time taken (hours): "))
        self.fuel = float(input("Enter fuel used (liters): "))

    def calculate_speed(self):
        return self.distance / self.time if self.time > 0 else 0

    def calculate_mileage(self):
        return self.distance / self.fuel if self.fuel > 0 else 0

    def display(self):
        print("\n----------- Car Details -----------")
        print(f"Brand           : {self.brand}")
        print(f"Model           : {self.model}")
        print(f"Distance (km)   : {self.distance}")
        print(f"Time (hrs)      : {self.time}")
        print(f"Fuel (liters)   : {self.fuel}")
        print(f"Speed (km/hr)   : {self.calculate_speed():.2f}")
        print(f"Mileage (km/l)  : {self.calculate_mileage():.2f}")
        print("----------------------------------")


def main():
    print("=== Car Information System ===")
    car = Car()
    car.input_details()
    car.display()


if __name__ == "__main__":
    main()