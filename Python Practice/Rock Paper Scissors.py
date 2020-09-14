import random as r

data = r.randint(0, 2)
computer = ["가위", "바위", "보"]

t = computer[data]
human = input("가위 바위 보 중 하나 입력 : ")
print("컴퓨터는 이걸 냈어 : ", t)

test_playing = True
while test_playing == True:

    if human == "가위":
        if t == 2:
            print("사람이 이김")
            break
    elif t == 0:
        if human == "보":
            print("컴퓨터가 이김")
            break
    elif human == "가위":
        if t == 0:
            print("비겼네 다시 해주세요")
            break
    elif human < t:
        print("컴퓨터가 이겼습니다!!")
        break
    elif t < human:
        print("사람이 이겼습니다!!")
        break
    elif t == human:
        print("비겼네 다시 해주세요")
        break
    else:
        print("다시 입력해주세요")
