"""def print_3_item():
    print("Hello")
    print("Hello")
    print("Hello")

print_3_item()"""

"""def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("juneha")"""

"""def print_n_times(n, *values):
    # n-bun-repeat.
    for i in range(n):
        # value nen list chuh rum hwal yong
        for value in values:
            print(value)
        # dansun jul bakkum
        print()

print_n_times(3, "annyeonghaseyo", "fun", "python")"""

"""def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("annyeonghaseyo", 5)"""

"""def test(a, b=10, c=100):
    print(a+b+c)

#1 basic form
test(10, 20, 30)

#2
test(c=10, a=100, b=200)

#3
test(c=10, a=100, b=200)

#4
test(10, c=200)"""

"""def return_test():
    for i in range(100):
        print(i)

    return i

return_test()"""

"""def sum_all(start, end):
    output = 0

    for i in range(start, end + 1):
        output += i

    return output

print("0 ~ 100:", sum_all(0, 100))
print("0 ~ 1000:", sum_all(0, 1000))
print("50 ~ 100:", sum_all(50, 100))
print("500 ~ 1000:", sum_all(500, 1000))"""

"""def factorial(n):

    output = 1

    for i in range(1, n+1):
         output *= i

    return output

print(factorial(453344))"""

"""def factorial_recurtion(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recurtion(n-1)

print("1!:", factorial_recurtion(1))
print("2!:", factorial_recurtion(2))
print("3!:", factorial_recurtion(3))
print("4!:", factorial_recurtion(4))
print("5!:", factorial_recurtion(5))"""

"""def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(50))"""

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

print("fibonacci(10)", fibonacci(10))
print("fibonacci(20)", fibonacci(20))
print("fibonacci(30)", fibonacci(30))
print("fibonacci(40)", fibonacci(40))
print("fibonacci(50)", fibonacci(50))"""

"""def flatten(data):
    output = []

    for d in data:
        if type(d) == list:
            output = output + flatten(d)
        else:
            output.append(d)

    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("change", flatten(example))"""

"""def hanoi(num, _from, _by, _to):

    if num == 1:
        print("{}에서 {}로 {} 번째 원반 이동".format(_from, _to, num))
        return

    hanoi(num-1, _from, _to, _by)
    print("{}에서 {}로 {} 번째 원반 이동".format(_from, _to, num))
    hanoi(num-1, _by, _from, _to)

if __name__ == "__main__":
    while 1:
        numOfTray = int(input("원반의 개수를 입력하세요(종료 : 0) :"))
        if numOfTray == 0:
            break
        hanoi(numOfTray, 'A', 'B', 'C')"""

