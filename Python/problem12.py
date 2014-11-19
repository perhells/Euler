import math

def divisors(n):
    i = 1
    count = 0
    sqrt = int(math.sqrt(n))
    while i <= sqrt:
        if i == sqrt:
            count = count + 1
            break
        if n % i == 0:
            count = count + 2
        i = i + 1
    return count

def largest(n):
    i = 1
    j = 1
    divisor = 1
    current = 1
    while divisor <= n:
        i = i + 1
        j = j + i
        current = divisors(j)
        if current > divisor:
            divisor = current
            print(str([j,divisor]))
    return j

print(str(largest(500)))
