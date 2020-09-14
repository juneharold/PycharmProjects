import primenumbers as pn
n = 0
primes = []
for i in range (100, 1000+1):
    if pn.isprime(i) is True:
        n += 1
        primes.append(i)

print("100부터 1000까지의 소수는 {}개".format(n))
print("100부터 1000까지의 소수:", primes)
