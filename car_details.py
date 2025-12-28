import sys
sys.stdout.reconfigure(encoding='utf-8')

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
        print(f"Price   : ₹{self.price}")


def main():
    script_name = sys.argv[0]

    # ✅ Default values in code
    brand = "HONDA"
    model = "CITY"
    speed = 200
    mileage = 10
    price = 5000000

    # ✅ If Jenkins provides parameters, override defaults
    if len(sys.argv) == 6:
        print("Using values provided by Jenkins parameters:\n")
        brand = sys.argv[1]
        model = sys.argv[2]
        speed = sys.argv[3]
        mileage = sys.argv[4]
        price = sys.argv[5]
    else:
        print("No Jenkins parameters given - using default values from code:\n")

    print("Script Name:", script_name)

    car = Car(brand, model, speed, mileage, price)
    car.display()


if __name__ == "__main__":
    main()
