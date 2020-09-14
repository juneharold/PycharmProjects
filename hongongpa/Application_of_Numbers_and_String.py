# 문자열의 format() 함수
"""print("{}".format(10))
print("{}{}{}{}".format(200, 40, 60, 5))"""

# format() 함수로 숫자를 문자열로 변환하기
"""string_a = "I am {} years old".format(10)

print(string_a)
print(type(string_a))"""

# format 함수의 다양한 형태
"""format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)"""

# IndexError
"""print("{} {}".format(1, 2, 3, 4, 5))
print("{} {} {}".format(1, 2))"""

# format() 함수의 다양한 기능

# 정수 출력의 다양한 형태
"""output_a = "{:d}".format(52)

output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

output_d = "{:05d}".format(52)
output_e = "{:d}".format(-52)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)"""

# 기호 붙혀 출력하기
"""output_f = "{:+d}".format(52)
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)


print(output_f)
print(output_g)
print(output_h)
print(output_i)"""

# 조합해 보기
"""output_h = "{:+5d}".format(52)
output_i = "{:+5d}".format(-52)
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)

print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)"""

# float 자료형 기본
"""output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:+015f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)
print(output_d)"""

# 소수점 아래 자릿수 지정하기
"""output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)"""

# 의미 없는 소수점 제거하기
"""output_a = 52.0
output_b = "{:g}".format(output_a)

print(output_a)
print(output_b)"""

# 대소문자 바꾸기: upper()와 lower()
"""a = "Hello World!"
print(a)
print(a.upper())
print(a.lower())"""

# 문자열 양옆의 공백 제거하기: strip()
"""input_a = ""
         Hello
World
""
print(input_a)
print(input_a.strip())"""

# 문자열의 구성 확인하기: isOO()
"""print("MANCHESTERUNITED7".isalnum())
print("2004".isdigit())
print("BDAY0605".isdigit())"""

# 문자열 찾기: find()와 rfind()
"""output_a = "안녕안녕하세요".find("안녕")
print(output_a)

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)

output_c = "안녕안녕하세요".find("203")
print(output_c)"""

# 문자열과 in 연산자
"""print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")"""

# 문자열 자르기:split()
"""a = "10 20 30 40 50".split(" ")
print(a)"""

