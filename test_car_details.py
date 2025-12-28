from car_details import Car, get_car_from_args

def test_default_values():
    car = get_car_from_args([])
    info = car.info()

    assert info["brand"] == "HONDA"
    assert info["model"] == "CITY"
    assert info["speed"] == 200
    assert info["mileage"] == 10.0
    assert info["price"] == 5000000.0


def test_custom_values():
    args = ["BMW", "X5", "240", "12", "8500000"]
    car = get_car_from_args(args)
    info = car.info()

    assert info["brand"] == "BMW"
    assert info["model"] == "X5"
    assert info["speed"] == 240
    assert info["mileage"] == 12.0
    assert info["price"] == 8500000.0


def test_type_conversion():
    car = Car("Audi", "A6", "220", "15.5", "7000000")
    info = car.info()

    assert isinstance(info["speed"], int)
    assert isinstance(info["mileage"], float)
    assert isinstance(info["price"], float)
