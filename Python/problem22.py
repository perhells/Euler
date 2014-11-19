import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1

names = open("names.txt","r").read().split(",")

for i in range(0,len(names)):
    names[i] = names[i].rstrip()
    names[i] = names[i].lstrip("\"")
    names[i] = names[i].rstrip("\"")

names.sort()

def value(name):
    result = 0
    for letter in name:
        result = result + values[letter.lower()]
    return result

def allvalues(namelist):
    result = 0
    count = 0
    for name in namelist:
        count = count + 1
        result = result + value(name) * count
    return result

print(allvalues(names))
