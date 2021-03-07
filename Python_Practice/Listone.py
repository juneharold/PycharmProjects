"""for a in range(1, 10):
    for b in range(1, 10):
        print(a, "x", b, "=", a*b)"""

"""array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
output = [[], [], [], [], []]

for number in array:
    output[(number+4)%5].append(number)

print(output)]"""


"""birthday = input("enter your birth year")

a = int(birthday)%12

if a == 4:
    print("mouse")
    
elif a == 5:
    print("cow")
    
elif a == 6:
    print("tiger")
    
elif a == 7:
    print("rabbit")
    
elif a == 8:
    print("dragon")
    
elif a == 9:
    print("snake")
    
elif a == 10:
    print("horse")
    
elif a == 11:
    print("sheep")
    
elif a == 0:
    print("monkey")

elif a == 1:
    print("chicken")

elif a == 2:
    print("dog")

else:
    print("pig")"""






"""dict_a = {
    "name": "avengers end game",

    "type": "hero movie"
}

print(dict_a["name"])

dict_b = {
    "director": ["anthony ruso", "Joe ruso"],

    "Cast": ["iron man", "thor", "thanos"]
}

print(dict_b["director"])
print(dict_b["Cast"])"""

"""dictionary = {

    "name": "7D Dried Mango",

    "type": "dang-zul-im",

    "ingredient": ["Mango", "Sugar", "meta-sodium-sulfur"],

    "origin": "philiphines"
}


print("name", dictionary["name"])
print("type", dictionary["type"])
print("ingredient", dictionary["ingredient"])
print("origin", dictionary["origin"])
print()

dictionary["name"] = "8D Dried Mango"
print("name:", dictionary["name"])

del dictionary ["origin"]
print(dictionary)"""

"""dictionary = {
    "name": "7D Dried Mango",
    "type": "dang-zul-im",
    "ingredient": ["Mango", "Sugar", "meta-sodium-sulfur"],
    "origin": "philiphines"
}

for key in dictionary:
    print(key, ":", dictionary[key])

value = dictionary.get("no such directory")
print("gab:", value)

if value == None:
    print("no such key exists")



key = input(">jub-gen hagoza hanun -ki:")

if key in dictionary:
    print(dictionary[key])
else:
    print("no such key exists")"""


"""array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in array:
    output[(number+2)%3].append(number)

dictionary = {
    "list_a": output
}

print(dictionary["list_a"])"""

"""pets = [
    {"name": "amuguna", "age": 7},
    {"name": "guna", "age": 8},
    {"name": "amu", "age": 9}
]

for pet in pets:
    print(pet["name"] + str(pet["age"]) + "sal")"""

"""for i in range(1, 10, 2):
    print(i)

list_a = [range(10)]
print(list_a)

print(list(range(10)))

print(list(range(0, 10, 2)))

array = [1, 2, 3, 4, 5]

for a in range(4, 0, -1):
    print("hyunjae banbok byunsu: {}".format(a))

for b in reversed(range(5)):
    print("hyunjae banbok byunsu: {}".format(b))

while True:
    print(".", end="")
    break

c = 0

while c < 10:
    print("hyunjae banbok byunsu: {}".format(c))
    c+=1"""

"""list_test = [1, 2, 1, 2]
value =2

while value in list_test:
    list_test.remove(value)

print(list_test)"""

"""import time

number = 0

target_tick = time.time() + 5

while time.time() < target_tick:
    number += 1

print("Repeated {}times in 5 seconds.".format(number))"""

i = 0
while True:
    print("repeated {} times".format(i))
    i = i + 1

    input_text = input(">close?(y):")
    if input_text in ["y", "Y"]:
        print("stop repeating")
        break

"""numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:

    if number < 10:
        continue
    elif number < 20:
        break
    print(number)"""