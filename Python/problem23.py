from math import sqrt

def isabundant(n):
    result = 1
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            if int(n / i) == int(sqrt(n)):
                result = result + i
            else:
                result = result + int(n/i) + i
            if result > n:
                return True
    return result > n

def generateabundant(n):
    numbers = [12]
    returnnumbers = set()
    for i in range(13,n):
        if isabundant(i):
            numbers.append(i)
    for i in numbers:
        for j in numbers:
            if i + j < n:
                returnnumbers.add(i+j)
            else:
                break
    return returnnumbers

def test(n):
    numbers = generateabundant(n)
    result = 0
    for i in range(1,n):
        if i not in numbers:
            #print(i)
            result = result + i
    return result

print(test(28124))
