# Exercise 1
import string

alphabet = " " + string.ascii_lowercase


# Exercise 2
positions = {}
for letter in alphabet:
    positions[letter] = alphabet.index(letter)


# Exercise 3
message = "hi my name is caesar"

encoded_message = ""
key_list = list(positions.keys())
val_list = list(positions.values())
for character in message:
    x = positions[character] + 1
    if x in val_list:
        encoded_message += key_list[val_list.index(x)]
    else:
        x = (positions[character] + 1) % 27
        encoded_message += key_list[val_list.index(x)]
print(encoded_message)


# Exercise 4
def encoding(message, key):
    encoded_message = ""
    global key_list
    global val_list
    for character in message:
        x = positions[character] + key
        if x in val_list:
            encoded_message += key_list[val_list.index(x)]
        else:
            x = (positions[character] + key) % 27
            encoded_message += key_list[val_list.index(x)]
    return encoded_message


key = 3
print(encoding(message, key))


# Exercise 5
decoded_message = encoding(encoded_message, -key)
print(decoded_message)