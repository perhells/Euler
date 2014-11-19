def fibevensum(n):
    first = 1
    second = 2
    result = 0
    while second < n:
        first, second = second, first + second
        if first % 2 == 0:
            result = result + first
    return result

print(str(fibevensum(4000000)))
