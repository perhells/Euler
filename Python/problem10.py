import math
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def sumofprimes(n):
    sum = 2
    for i in range(3,n):
        if isprime(i):
            sum = sum + i
    return sum

print(str(sumofprimes(2000000)))
