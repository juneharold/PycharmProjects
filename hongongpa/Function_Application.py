# 팩토리얼 함수 만들어보기
"""def factorial(n):

    output = 1

    for i in range(1, n + 1):
        output *= i

    return output


print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))"""

# 재귀 함수를 사용해 팩토리얼 구하기
"""def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))"""

# 재귀 함수로 구현한 피보나치 수열(1)
"""def fibonacci(n):

    if n == 1:
        return 1
    if n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
import time
sigan = time.time()
print("fibonacci(35):", fibonacci(35))
print(time.time() - sigan)"""

# 재귀 함수로 구현한 피보나치 수열(2)
"""counter = 0


def fibonacci(n):

    print("fibonacci({})을 구합니다.".format(n))
    global counter
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))"""

# UnboundLocalError에 대한 처리 [재귀 함수로 구현한 피보나치 수열(3)]
"""counter = 0


def fibonacci(n):

    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))"""

# 메모화
"""dictionary = {
    1: 1,
    2: 2
}


def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:

        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output


print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))"""

# 문제 1


"""def flatten(data):
    output = []
    for each_item in data:
        if type(each_item) == list:
            output += flatten(each_item)
        else:
            output.append(each_item)
    return output


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))"""

# 문제 2


앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 = 10
전체사람의수 = 100
memo = {"one": 1}


def 문제(남은사람수, 앉힌사람수):
    key = str([남은사람수, 앉힌사람수])

    if key in memo:
        return memo[key]
    if 남은사람수 < 0:
        return 0
    if 남은사람수 == 0:
        return 1

    count = 0
    for i in range(앉힌사람수, 앉힐수있는최대사람수 + 1):
        count += 문제(남은사람수 - i, i)

    memo[key] = count

    return count


print(문제(전체사람의수, 앉힐수있는최소사람수))