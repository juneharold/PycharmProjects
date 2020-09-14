# 딕셔너리 선언하기/요소에 접근하기
"""dict_a = {
    "name": "어벤저스 엔드게임",
    "type": "히어로 영화"
}

print(dict_a)
print(dict_a["name"])
print(dict_a["type"])"""

"""dict_b = {
    "director": ["안소니 루소", "조 루소"],
    "cast": ["아이언맨", "타노스", "토르", "닥터 스트레인지", "헐크", "캡틴 아메리카"]
}

print(dict_b)
print(dict_b["director"])
print(dict_b["type"])"""

# 딕셔너리 요소에 접근하기
"""dictionary = {
    "name": "7D Dried Mango",
    "type": "Sugary snack",
    "ingredient": ["mango", "sugar", "sodium", "food coloring"],
    "origin": "Philippines "
}

print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])

dictionary["name"] = "8D Dried Mango" #값을 변경합니다"""

# NameError
"""dict_key = {
    name: "Dried Mango",
    type: "Sugar snack"
}
print(dict_key)"""

# Solving NameError (잘 안씀)
"""name = "이름"

dict_key = {
    name: "Dried Mango",
    type: "Sugar snack"
}
print(dict_key)"""

# 딕셔너리에 값 추가하기/제거하기
"""dictionary = {
    "name": "7D Dried Mango",
    "type": "Sugary snack",
    "ingredient": ["mango", "sugar", "sodium", "food coloring"],
    "origin": "Philippines "
}

dictionary["price"] = "700 yen"

print(dictionary)
print()

del dictionary["ingredient"]
print(dictionary)"""

"""dictionary = {}
print("요소 추가 이전:", dictionary)

dictionary["name"] = "Harold"
dictionary["age"] = "35"
dictionary["height"] = "185"

print("요소 추가 이후:", dictionary)
print()

print("요소 제거 이전:", dictionary)

del dictionary["name"]
del dictionary["age"]
del dictionary["height"]

print("요소 제거 이후:", dictionary)"""

# KeyError
"""dictionary = {}
print(dictionary["key"])"""

# 키가 존재하는지 확인하고 값에 접근하기
"""dictionary = {
    "name": "7D Dried Mango",
    "type": "Sugary snack",
    "ingredient": ["mango", "sugar", "sodium", "food coloring"],
    "origin": "Philippines "
}

key = input("접근하고자 하는 키 >")
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")"""

# get() 함수 - 키가 존재하지 않을 때 None을 출력하는지 확인하기
"""dictionary = {
    "name": "7D Dried Mango",
    "type": "Sugary snack",
    "ingredient": ["mango", "sugar", "sodium", "food coloring"],
    "origin": "Philippines "
}

value = dictionary.get("존재하지 않는 키")
print("값:", value)

if value == None:
    print("존재하지 않는 키에 접근하고 있습니다.")"""

# for 반복문과 딕셔너리
"""dictionary = {
    "name": "7D Dried Mango",
    "type": "Sugary snack",
    "ingredient": ["mango", "sugar", "sodium", "food coloring"],
    "origin": "Philippines "
}

for key in dictionary:
    print(key, ":", dictionary[key])"""

# 문제 2
"""pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]

print("#우리 동네 애완 동물들")
for key in pets:
    print(key["name"], key["age"], "살")"""

# 문제 3
"""numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}

for number in numbers:
    if number not in counter:
        counter[number] = 1
    else:
        counter[number] += 1

print(counter)"""

# 문제 4
"""character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for n in character[key]:
            print(n, ":", character[key][n])
    elif type(character[key]) is list:
        for element in character[key]:
            print(key, ":", element)
    else:
        print(key, ":", character[key])"""

# Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

                # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    game()