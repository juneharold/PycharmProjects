# 매개변수와 범위
"""a = range(5)
print(a)
print(list(a))
print(list(range(0, 5)))
print(list(range(5, 10)))
print(list(range(0, 10, 2)))"""

"""10을 포함할 것을 강조하기"""
"""a = range(0, 10+1)
print(list(a))"""

# range() 함수에 나누기 연산자를 사용한 경우 --> TypeError
"""n = 10
a = range(0, int(n/2))
print(list(a))

b = range(0, n//2)
print(list(b))"""

# for 반복문과 범위
"""for i in range(5):
    print(str(i), "= 반복 변수")
print()

for i in range(5, 10):
    print(str(i), "= 반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i), "= 반복 변수")
print()"""

# for 반복문: 리스트와 범위 조합하기
"""array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    print("{}는 {}번째".format(array[i], i))"""

# 반대로 반복하기 1
"""for i in range(4, 0 - 1, -1):
    print("현재 반복 변수: {}".format(i))"""

# 반대로 반복하기 2
"""for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))"""

# while 반복문
"""while True:
    print(".", end="")"""

# while 반복문: for 반복문처럼 사용하기
"""i = 0
while i < 10:
    print("{}번째 반복입니다".format(i))
    i += 1"""

# while 반복문: 상태를 기반으로 반복하기
"""list_test = [1, 2, 1, 2]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)"""

# while 반복문: 시간을 기반으로 반복하기
"""import time
print(time.time())"""

# 5초 동안 반복하기
"""import time
number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복함".format(number))"""

# while 반복문: break/continue 키워드
"""i = 0

while True:
    print("{}번째 반복문입니다".format(i))
    i += 1

    input_text = input("종료하시겠습니까?(y):")
    if input_text in ["y", "Y"]:
        print("반복 종료")
        break"""

"""numbers = [1, 3, 34, 24, 10, 12]

for number in numbers:
    if number <= 10:
        continue

    print(number)"""

# 문제 2
"""key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 300, 23, 5]
character = {}

for a in range(len(key_list)):
        character[key_list[a]] = value_list[a]

print(character)"""

# 문제 3
"""hangae = input("한계를 입력하시오:")
limit = int(hangae)
i = 0

while i <= limit:
    for n in range(0, limit):
        i += n
        if i > limit:
            break

print("1부터 {}까지 더했을 때 {}를 넘으며 그때의 값은{}".format(n, limit, i))"""


"""limit = 10000
i = 1

sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1

print("{}번 더했을 때 {}를 넘으며 그때의 값은{}".format(i, limit, sum_value))"""

# 문제 4
max_value = 0
a = 0
b = 0

for i in range(1, 100+1):
    j = 100 - i

    if i*j > max_value:
        max_value = i*j
        a = i
        b = j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

