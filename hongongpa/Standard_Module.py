# math 모듈
"""import math

print("sin(1)=", math.sin(1))
print("cos(1)=", math.cos(1))
print("tan(1)=", math.tan(1))
print("log(32, 2)=", math.log(32, 2))
print("2.5 올림:", math.ceil(2.5))
print("2.5 내림:", math.floor(2.5))"""

# from 구문
"""from math import sin, cos, tan, floor, ceil, log

print("sin(1)=", sin(1))
print("cos(1)=", cos(1))
print("tan(1)=", tan(1))
print("log(32, 2)=", log(32, 2))
print("2.5 올림:", ceil(2.5))
print("2.5 내림:", floor(2.5))"""

# as 구문
"""import math as m

print("sin(1)=", m.sin(1))
print("cos(1)=", m.cos(1))
print("tan(1)=", m.tan(1))
print("log(32, 2)=", m.log(32, 2))
print("2.5 올림:", m.ceil(2.5))
print("2.5 내림:", m.floor(2.5))"""

# random 모듈
"""import random
print("# random 모듈")


# random(): 0.0 <= x < 1.0 사이의 float를 리턴합니다.
print("- random():", random.random())


# uniform(min, max): 지정한 범위 사이의 float를 리턴합니다.
print("- uniform(10, 20):", random.uniform(10, 20))

# randrange(): 지정한 범위의 int를 리턴합니다.
# - randrange(max): 0부터 max 사이의 값을 리턴합니다.
# - randrange(min, max): min부터 max 사이의 값을 리턴합니다.
print("- randrange(10):", random.randrange(10))

# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))

# shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다.
print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))

# sample(list, k=<숫자>): 리스트의 요소 중에서 k개를 뽑습니다.
print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))"""

# sys 모듈
"""import sys
print(sys.argv)
print("---")

print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

sys.exit()"""

# os 모듈
"""import os

# 기본 정보를 몇개 출력해 봅시다.
print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

# 폴더를 만들고 제거합니다 [폴더가 비어있을 때만 제거 가능].
os.mkdir("hello")
os.rmdir("hello")

# 파일을 생성하고 + 파일 이름을 변경합니다.
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일을 제거합니다.
os.remove("new.txt")

# 시스템 명령어 실행 ["ls" for mac instead of "dir"]
os.system("ls")"""

# datetime 모듈
"""import datetime

print("# 현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d.%H.%M.%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
output_c = now.strftime("%Y %m %d %H %M %S").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)
print()"""

# 시간 처리하기
"""import datetime
now = datetime.datetime.now()

print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))"""

# time 모듈
"""import time
print("지금부터 5초 동안 정지합니다!")
time.sleep(5)
print("프로그램을 종료합니다")"""

# urllib 모듈
"""from urllib import request

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

target = request.urlopen("https://google.com")
output = target.read()

print(output)"""

# 문제 3
import os


def read_folder(path):

    output = os.listdir(path)

    for item in output:
        if os.path.isdir(item):
            read_folder(item)
        else:
            print("파일:", item)


read_folder(".")

