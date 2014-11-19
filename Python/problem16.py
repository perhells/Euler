def powersum(n):
    number = 2**n
    tostring = str(number)
    sum = 0
    for i in range(0,len(tostring)):
        sum = sum + int(tostring[i])
    return sum

print(str(powersum(int(input("Enter a number: ")))))
