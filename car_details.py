import sys

class Car:
    def __init__(self, brand, model, speed, mileage, price):
        self.brand = brand
        self.model = model
        self.speed = int(speed)
        self.mileage = float(mileage)
        self.price = float(price)

    def display(self):
        print("\n=== Car Information System ===")
        print(f"Brand   : {self.brand}")
        print(f"Model   : {self.model}")
        print(f"Speed   : {self.speed} km/h")
        print(f"Mileage : {self.mileage} km/l")
        print(f"Price   : {self.price}")


def main():
    if len(sys.argv) != 6:
        print("Usage: python car_details.py <brand> <model> <speed> <mileage> <price>")
        sys.exit(1)

    _, brand, model, speed, mileage, price = sys.argv
    car = Car(brand, model, speed, mileage, price)
    car.display()


if __name__ == "__main__":
    main()
