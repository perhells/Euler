def fib(n):
    previous = 1
    current = 1
    index = 2
    while len(str(current)) < n:
        temp = current
        current = current + previous
        previous = temp
        index += 1
    print current
    print index

fib(1000)
