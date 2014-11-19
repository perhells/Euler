import math
def triplet(n):
    i = 1
    j = 1
    while i <= 1000:
        sum = 0
        while sum <= 1000:
            k = math.sqrt(i*i+j*j)
            sum = i + j + k
            if sum == 1000:
                return [i,j,k]
            j = j + 1
        i = i + 1
        j = 1
    return [0,0,0]

print(str(triplet(1000)))
