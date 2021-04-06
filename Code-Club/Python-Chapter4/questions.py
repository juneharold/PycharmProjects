import random as r

a=r.randint(1, 100)

print(a)

sum=0
for i in range(0, a):
    num=r.randint(0, 10000000)
    sum+=num
    print(num, end=" ")

print("\n")
print(sum)

