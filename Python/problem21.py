import math

def divisorsum(n):
    result = 1
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            result = result + i + int(n/i)
    return result

def isamicable(n):
    first = divisorsum(n)
    second = divisorsum(first)
    if n == second and not first == second:
        return True
    else:
        return False

def amicsum(n):
    result = 0
    for i in range(1,n):
        if isamicable(i):
            result = result + i
    return result

print(amicsum(10000))
