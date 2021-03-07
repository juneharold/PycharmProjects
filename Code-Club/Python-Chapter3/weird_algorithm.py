n = int(input())

print(n, end=" ")
while n > 1:
    if n % 2 == 0:
        n = n/2
        print(int(n), end=" ")
    elif n % 2 == 1:
        n = n*3 + 1
        print(int(n), end=" ")

