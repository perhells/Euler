import math

def primefactors(n):
    primes = []
    done = False
    while not done:
        done = True
        for i in range(2,int(math.sqrt(n))):
            if n % i == 0:
                primes.append(i)
                n = int(n / i)
                done = False
    if n > 1:
        primes.append(n)
    return primes

print(str(primefactors(28)))
