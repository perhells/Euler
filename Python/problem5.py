def iscool(n):
    for x in reversed(range (2,21)):
        if not n % x == 0:
            return False
    return True

def findsmallest():
    factor = 2*3*5*7*11*13*17*19
    smallest = factor
    while True:
        if iscool(smallest):
            return smallest
        smallest = smallest + factor

print(str(findsmallest()))
