import sys
sys.stdout.reconfigure(encoding='utf-8')

class Car:
    def __init__(self, brand, model, speed, mileage, price):
        self.brand = brand
        self.model = model
        self.speed = int(speed)
        self.mileage = float(mileage)
        self.price = float(price)

    def info(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "speed": self.speed,
            "mileage": self.mileage,
            "price": self.price
        }

    def display(self):
        print("\n=== Car Information System ===")
        print(f"Brand   : {self.brand}")
        print(f"Model   : {self.model}")
        print(f"Speed   : {self.speed} km/h")
        print(f"Mileage : {self.mileage} km/l")
        print(f"Price   : {self.price}")


def get_car_from_args(args):
    # default values
    brand = "HONDA"
    model = "CITY"
    speed = 200
    mileage = 10
    price = 5000000

    if len(args) == 5:
        brand, model, speed, mileage, price = args

    return Car(brand, model, speed, mileage, price)


def main():
    print("Script Name:", sys.argv[0])

    if len(sys.argv) == 6:
        print("Using values provided by Jenkins parameters:\n")
        car = get_car_from_args(sys.argv[1:])
    else:
        print("No Jenkins parameters given - using default values from code:\n")
        car = get_car_from_args([])

    car.display()


if __name__ == "__main__":
    main()
