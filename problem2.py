cars = {
    "Cobalt": {"narx": 12000, "yil": 2022},
    "Malibu": {"narx": 25000, "yil": 2023},
    "Damas": {"narx": 9000, "yil": 2021},
}
def the_cheapest_car(car_dict):
    cheap = list(car_dict.items())[0]
    for car, info in car_dict.items():
        if info["narx"] < cheap[1]["narx"]:
            cheap = (car, info)
    return cheap

def the_newest_car(car_dict):
    new = list(car_dict.items())[0]
    for car, info in car_dict.items():
    
        if info["yil"] > new[1]["yil"]:
            new = (car, info)
            return new

cheap = the_cheapest_car(cars)
print(f"Eng arzon mashina: {cheap[0]}, narxi: {cheap[1]['narx']}$")

new = the_newest_car(cars)
print(f"Eng yangi mashina: {new[0]}, yili: {new[1]['yil']}")
