import math

temp = math.factorial(100)

string = str(temp)

result = 0

for i in string:
    result = result + int(i)

print(result)
