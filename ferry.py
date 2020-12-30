import random

Purple = 0
Green = 0
Yellow = 0
Blue = 0
Red = 0
Bike = 0

num_vehicle_list = []
space_left_list = []

for i in range(1000):
    area = 0
    vehicle_num = 0
    while True:
        number = random.randint(1, 100)
        if number <= 10:
            area += 3
        elif number <= 25:
            area += 4
        elif number <= 30:
            area += 1
        elif number <= 75:
            area += 2
        elif number <= 90:
            area += 6
        else:
            area += 5
        vehicle_num += 1
    print(area)
    num_vehicle_list.append(vehicle_num)
    space_left = (100 - area)
    space_left_list.append(vehicle_num)




