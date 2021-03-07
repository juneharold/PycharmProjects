"""example_list = ["element A", "element B", "element C"]

print("#print")
print(example_list)
print()

print("#enumberate()applied function print")
print(enumerate(example_list))
print()

print("#list() FORCED TO CHANGE PRINT FUNCTION")
print(list(enumerate(example_list)))
print()

print("#combination")
for i, value in enumerate(example_list):
    print("{}th element is {}".format(i, value))

print()
print()
print()

example_dictionary = {
    "key A": "value A",
    "key B": "value B",
    "key C": "value C"
}

print("#dictionary의 items() function")
print("items():", example_dictionary. items())
print()
print("#dictionary의 items() function and ban bok mun combination")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))

numbers = [1, 2, 1, 3, 4, 5, 1, 2, 6, 2, 7, 9, 10, 2, 3, 7, 6, 3, 8, 9]
counter = {}

for a in numbers:
    if a in counter:
        counter[a] = counter[a] + 1

    else:
        counter[a] = 1

print(counter)


character = {
    "name": "Gisa",
    "level": 30,
    "items": {
        "sword": "sword of fire",
        "armor": "full plate"
    },
    "ingredient": {
        "2 cha zun zik": "hero",
        "3 cha zun zik": "Paladin",
        "4 cha zun zik": "Dark Knight"
    },
    "skill": ["cut", "strong cut", "very strong cut"]
}

for key in character:
    if type(character[key]) is dict:
        for all_dict in character[key]:
            print(key, ":", character[key][all_dict])

    elif type(character[key]) is list:
        for all_list in character[key]:
            print(key, ":", all_list)

    else:
        print(key, ":", character[key])

key_list = ["name", "HP", "mp", "level"]
value_test = ["juneha", 1, 1, 1]
character = {}

for a in range(len(key_list)):
    character[key_list[a]] = value_test[a]

print(character)"""


for i in range(100):
    j = 100 - i
    if j == i:
        print("최대가 되는 경우 : {} * {} = {}".format(i, j, j*i))
