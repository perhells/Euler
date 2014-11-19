size = 0

def paths(n):
    previous=[1]
    current=[1]
    for i in range(2,n+1):
        previous = current
        current = [1,i+1]
        for j in range(2,len(previous)):
            current.append(previous[j]+current[j-1])
        current.append(current[-1]*2)
        #print(str(current))
    return current[-1]

size = int(input("Select grid size (X*X): "))
print([size,paths(size)])
