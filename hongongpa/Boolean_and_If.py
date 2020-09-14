# 비교 연산자
"""print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)

print("가방" == "가방")
print("가방" != "하마")
print("가방" < "하마")
print("가방" > "하마")"""

# 범위 구하기
"""x = 15
print(10<x<20)
print(30<x<20)"""

# 논리 연산자: not
"""print(not True)
print(not False)

x = 10
y = 1.5
under_20 = x*y < 20
print("under 20:", under_20)
print("not under 20:", not under_20)"""

# 논리 연산자: and, or
"""print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)"""

# if 조건문
"""number = input("정수 입력")
number = int(number)

if number > 0:
    print("양수우우우우우")
if number == 0:
    print("영ㅇㅇㅇ")
if number < 0:
    print("음수우우우우우")"""

# 날짜/시간 출력하기
"""import datetime
now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print(type(now))"""

# 날짜/시간 한 줄로 출력하기
"""import datetime
now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}.{}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second,
    now.microsecond,
))"""

# 오전과 오후를 구분하는 프로그램
"""import datetime
now = datetime.datetime.now()

if now.hour < 12:
    print("오전 {}시입니다".format(now.hour))

if now.hour >= 12:
    print("오후 {}시입니다".format(now.hour))"""

# 계절을 구분하는 프로그램
"""import datetime
now = datetime.datetime.now()

if (now.month == 12) or (1 <= now.month <= 2):
    print("현재는 {}월로 겨울입니다.".format(now.month))

if 3 <= now.month <= 5:
    print("현재는 {}월로 봄입니다.".format(now.month))

if 6 <= now.month <= 8:
    print("현재는 {}월로 여름입니다.".format(now.month))

if 9 <= now.month <= 11:
    print("현재는 {}월로 가을입니다.".format(now.month))"""

# 끝자리로 짝수와 홀수 구분
"""number = input("정수 입력 > ")

last_character = number[-1]

last_number = int(last_character)

if last_number == 0 \
    or last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수입니다")

else:
    print("홀수입니다")"""

# in 문자열 연산자를 이용하여 구분하기
"""number = input("정수 입력 > ")

last_character = number[-1]

if last_character in "02468":
    print("짝수입니다")
if last_character in "13579":
    print("홀수입니다")"""

# 나머지 연산자를 이용하여 짝수와 홀수 구분
number = input("정수 입력 > ")
number = int(number)

if number % 2 == 0:
    print("짝수입니다")
if number % 2 == 1:
    print("홀수입니다")