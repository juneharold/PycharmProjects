# if 조건문에 else 구문을 추가해서 짝수와 홀수 구분
"""number = input("정수 입력 > ")
number = int(number)

if number % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")"""

# 계절 구하기
"""import datetime
now = datetime.datetime.now()

if (now.month == 12) or (1 <= now.month <= 2):
    print("현재는 {}월로 겨울입니다.".format(now.month))

elif 3 <= now.month <= 5:
    print("현재는 {}월로 봄입니다.".format(now.month))

elif 6 <= now.month <= 8:
    print("현재는 {}월로 여름입니다.".format(now.month))

else:
    print("현재는 {}월로 가을입니다.".format(now.month))"""

# 학점 구하기
"""score = float(input("Enter your GPA: "))

if score == 4.5:
    print("당신은 god 입니다")
elif 4.2 <= score < 4.5:
    print("당신은 loved by professor 입니다")
elif 3.5 <= score < 4.2:
    print("당신은 guardian of current system 입니다")
elif 2.8 <= score < 3.5:
    print("당신은 normal 입니다")
elif 2.3 <= score < 2.8:
    print("당신은 Playa 입니다")
elif 1.75 <= score < 2.3:
    print("당신은 gaming pioneer 입니다")
elif 1.0 <= score < 1.75:
    print("당신은 peasant 입니다")
elif 0.5 <= score < 1.0:
    print("당신은 looper 입니다")
elif 0 < score < 0.5:
    print("당신은 plankton 입니다")
elif score == 0:
    print("당신은 innovator seed from the future 입니다")
else:
    print("you are a liar!")"""

# False로 변환되는 값
"""print("#if 조건문에 0 넣기")
if 0:
    print("O은 True 로 변환됩니다")
else:
    print("0은 False 로 변환됩니다")
print()

print("#if 조건문에 빈 문자열 넣기")
if 0:
    print("빈 문자열은 True 로 변환됩니다")
else:
    print("빈 문자열은 False 로 변환됩니다")"""

# pass 키워드
"""number = int(input("정수 입력 > "))

if number > 0:
    pass
else:
    pass"""
# raise NotImplementError
number = int(input("정수 입력 > "))

if number > 0:
    raise NotImplementError
else:
    raise NotImplementError
