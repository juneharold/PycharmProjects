# 리스트
"""array = [273, 32, 103, "문자열", True, False]
print(array)"""

# 인덱스
"""list_a = [273, 32, 103, "문자열", True, False]
print(list_a[3])
print(list_a[0])
print(list_a[2:6])"""

# 요소 변경하기
"""list_a = [273, 32, 103, "문자열", True, False]
list_a[0] = 2004

print(list_a)"""

# 대괄호 안에 음수 넣어 사용하기
"""list_a = [273, 32, 103, "문자열", True, False]
print(list_a[-1])
print(list_a[-4])
print(list_a[-5])"""

# 리스트 접근 연산자 이중으로 사용하기
"""list_a = [273, 32, 103, "문자열", True, False]
print(list_a[3])
print(list_a[3][0])"""

# 리스트 안에 리스트
"""list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_a[1])
print(list_a[1][2])"""

# IndexError
"""list_a = [273, 32, 103, "문자열", True, False]
print(list_a[6])"""

# 리스트 연산자: 연결(+), 반복(*), len()
"""list_a = [1, 2, 3]
list_b = [4, 5, 6]
print("#리스트")
print("list_a = ", list_a)
print("list_b = ", list_b)
print()

print("#리스트 기본 연산자")
print("list_a + list_b = ", list_a + list_b)
print("list_a * 3 = ", list_a * 3)
print()

print("#길이 구하기")
print("len(list_a) = ", len(list_a))"""

# 리스트에 요소 추가하기
"""list_a = [1, 2, 3]

print("#리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("#리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)"""

# extend() 함수
"""list_a = [1, 2, 3]
list_a.extend([4, 5, 6])
print(list_a)"""

# 인덱스로 제거하기: del, pop
"""list_a = [0, 1, 2, 3, 4, 5]
print("#리스트의 요소 하나 제거하기")

del list_a[1]
print("del list_a[1]를 했을 때: ", list_a)

list_a.pop(2)
print("list_a.pop(2)를 했을 때: ", list_a)"""

# del 키워드로 범위 지정해서 지우기
"""list_b = [0, 1, 2, 3, 4, 5, 6]
list_c = [0, 1, 2, 3, 4, 5, 6]
list_d = [0, 1, 2, 3, 4, 5, 6]
print("#리스트의 요소 여러개 제거하기")

del list_b[3:6]
print(list_b)

del list_c[:3]
print(list_c)

del list_d[3:]
print(list_d)"""

# 값으로 제거하기: remove
"""list_a = [1, 2, 1, 2]
list_a.remove(2)
print(list_a)"""

# 모두 제거하기: clear
"""list_d = [0, 1, 2, 3, 4, 5]
list_d.clear()
print(list_d)"""

# 리스트 내부에 있는지 확인하기: in/not in 연산자
"""list_a = [273, 32, 103, 57, 59]

print(273 in list_a)
print(2004 in list_a)

print(273 not in list_a)
print(100 not in list_a)"""

# for 반복문
"""for i in range(100):
    print("출력")"""

# for 반복문과 리스트
"""array = [273, 32, 103, 57, 52]

for element in array:
    print(element)"""

# 3번 문제
"""numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number%2 == 0:
        print("{}는 짝수입니다".format(number))
    else:
        print("{}는 홀수입니다".format(number))"""

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number >= 100:
        print("{}는 3자릿수입니다".format(number))
    elif number >= 10:
        print("{}는 2자릿수입니다".format(number))
    else:
        print("{}는 1자릿수입니다".format(number))

# 4번 문제
"""list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9],
]

for a in list_of_list:
    for b in a:
        print(b)"""
