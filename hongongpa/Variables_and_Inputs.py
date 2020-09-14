# 변수 만들기/사용하기
"""pi = 3.14159265
print(pi)
print(pi+2)
print(pi/3)
print(pi*pi)"""

# 원의 둘레와 넓이 구하기
"""pi = 3.14159265
r=10

print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2*pi*r)
print("원의 넓이 =", pi*r**2)"""

# 복합 대입 연산자
"""number = 100
number += 10
number *= 2
number /= 11
print("number:", number)"""

# 문자열 복합 대입 연산자
"""string = "Hello"
string += "!"
string *= 3
print("string:", string)"""

# 사용자 입력: input()
"""string = input("Say Something:")
print(string)"""

# input() 함수의 입력 자료형
"""number = input("숫자를 입력하세요")
print(number)
print(type(number))"""

"""string = input("입력:")
print(string)
print("자료형:", type(string))"""

# TypeError
"""string = input("입력:")
print("입력 + 100:", string + 100)"""

# 문자열을 숫자로 바꾸기:

# int() 함수 활용하기
"""string_a = input("입력A: ")
int_a = int(string_a)

string_b = input("입력B: ")
int_b = int(string_b)

print("문자열 자료:", string_a+string_b)
print("숫자형 자료:", int_a+int_b)"""

# int() 함수와 float() 함수 활용하기
"""output_a = int("2004")
output_b = float("6.05")

print(type(output_a), output_a)
print(type(output_b), output_b)"""

# int() 함수와 float() 함수 조합하기
"""input_a = float(input("첫 번째 숫자: "))
input_b = float(input("두 번째 숫자: "))

print("덧셈 결과:", input_a+input_b)
print("뺄셈 결과:", input_a-input_b)
print("곱셈 결과:", input_a*input_b)
print("나눗셈 결과:", input_a/input_b)"""

# 숫자를 문자열로 바꾸기
"""output_a = str(2004)
output_b = str(6.05)
print(type(output_a), output_a)
print(type(output_b), output_b)"""

# Question 6 of Textbook
a = input("문자열 입력:")
b = input("문자열 입력:")

print(a, b)

c = a # 새로운 변수 c를 쓴다.
a = b
b = c

print(a, b)