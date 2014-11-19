def fivethree(n):
    result = 0
    for x in range(1,n):
        if x % 3 == 0 or x % 5 == 0:
            result = result + x
    return result

number = int(input("Enter a number: "))
print("The sum of the numbers up to " + str(number) + " is: " + str(fivethree(number)))
