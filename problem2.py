cars = {
    "Cobalt": {"narx": 12000, "yil": 2022},
    "Malibu": {"narx": 25000, "yil": 2023},
    "Damas": {"narx": 9000, "yil": 2021},
}

def the_newest_car(car_dict):
    new = list(car_dict.items())[0]
    for car, info in car_dict.items():
    
        if info["yil"] > new[1]["yil"]:
            new = (car, info)
            return new

new = the_newest_car(cars)
print(f"Eng yangi mashina: {new[0]}, yili: {new[1]['yil']}")
