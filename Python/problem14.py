def collatz(n):
    numbers = [n]
    while n > 1:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = n * 3 + 1
        numbers.append(n)
    return len(numbers)

def longest(n):
    biggest = 0
    length = 0
    for i in range(1,n):
        current = collatz(i)
        if current > length:
            print([i,current])
            biggest = i
            length = current
    return [biggest,length]

print(str(longest(1000000)))
