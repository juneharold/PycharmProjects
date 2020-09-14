# 리스트에 적용할 수 있는 기본 함수: min(), max(), sum()
"""numbers = [34, 23, 523, 21, 9]

print(min(numbers))
print(max(numbers))
print(sum(numbers))"""

# reversed() 함수로 리스트 뒤집기
"""list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("#reversed() 함수")
print("reversed([1, 2, 3, 4, 5]):", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
print()

print("#reversed 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed([1, 2, 3, 4, 5]):
    print("-", i)"""

# 확장 슬라이싱
"""numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[::-1])"""

# enumerate() 함수와 반복문 조합하기
"""example_list = ["element 1", "element 2", "element 3"]
for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다".format(i, example_list[i]))"""

"""example_list = ["요소A", "요소B", "요소C"]

print("# 단순 출력")
print(example_list)
print()

print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))"""

# 딕션너리의 items() 함수와 반복문
"""example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C"
}

print("# 딕션너리의 items() 함수")
print("items():", example_dictionary.items())
print()

print("딕션너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))"""

# 반복문을 사용한 리스트 생성
"""array = []

for i in range(0, 20, 2):
    array.append(i*i)

print(array)"""

# 리스트 안에 for문 사용하기
"""array = [i * i for i in range(0, 20, 2)]

print(array)"""

# 조건을 활용한 리스트 내포
"""array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

print(output)"""

# if 조건문과 여러 줄 문자열(1)
"""number = int(input("정수 입력:"))

if number % 2 ==0:
    print("\
    입력한 문자열은 {}입니다.
    {}은 짝수입니다".format(number, number))

else:
    print("\
    입력한 문자열은 {}입니다.
    {}은 홀수입니다".format(number, number))"""

# if 조건문과 여러 줄 문자열(2)
"""number = int(input("정수 입력:"))

if number % 2 ==0:
    print("입력한 문자열은 {}입니다.
{}은 짝수입니다".format(number, number))
else:
    print("입력한 문자열은 {}입니다.
{}은 홀수입니다".format(number, number))"""

# if 조건문과 긴 문자열
"""number = int(input("정수 입력:"))

if number % 2 ==0:
    print("입력한 문자열은 {}입니다.\n{}은 짝수입니다".format(number, number))
else:
    print("입력한 문자열은 {}입니다.\n{}은 홀수입니다".format(number, number))"""

# 괄호로 문자열 연결하기
"""test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성됩니다"
)

print("test:", test)
print("type(test):", type(test))"""

# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(1)
"""number = int(input("정수 입력:"))

if number % 2 == 0:
    print((
              "입력한 문자열은 {}입니다.\n"
              "{}은 짝수입니다"
    ).format(number, number))
else:
    print((
              "입력한 문자열은 {}입니다.\n"
              "{}은 홀수입니다"
    ).format(number, number))"""

# 문자열의 join() 함수
"""print("::".join(["1", "2", "3", "4", "5"]))"""

# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(2)
"""number = int(input("정수 입력:"))

if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}은 짝수입니다"
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}은 홀수입니다"
    ]).format(number, number))"""

# reversed() 함수와 이터레이터
"""numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print("reversed numbers:", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))"""

# 문제 2
output = [t for t in range(0, 100 + 1) if "{:b}".format(t).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))


