cars = {
    "Cobalt": {"narx": 12000, "yil": 2022},
    "Malibu": {"narx": 25000, "yil": 2023},
    "Damas": {"narx": 9000, "yil": 2021},
}


def the_cheapest_car(car_dict):
    return min(car_dict.items(), key=lambda x: x[1]["narx"])
    
def the_newest_car(car_dict):
    return max(car_dict.items(), key=lambda x: x[1]["yil"])

cheap_car = the_cheapest_car(cars)
print(f"The cheapest car: {cheap_car[0]}, narxi: {cheap_car[1]["narx"]}$")

new_car = the_newest_car(cars)
print(f"The newest  car: {new_car[0]}, yili: {new_car[1]["yil"]}")