def sumSquareDifference(n):
    return squareOfSum(n) - sumOfSquares(n)

def sumOfSquares(n):
    result = 0
    for i in range(1,n+1):
        result = result + i * i
    return result

def squareOfSum(n):
    result = 0
    for i in range(1,n+1):
        result = result + i
    result = result * result
    return result

print(str(sumSquareDifference(100)))
