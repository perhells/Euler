import math
def prime(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        addable = True
        for div in primes:
            if div > math.sqrt(i):
                break
            if i % div == 0:
                addable = False
        if addable:
            primes.append(i)
        i = i + 1
    print(str(primes))
    return primes[-1]

print(str(prime(int(input("Which prime number do you seek? ")))))
