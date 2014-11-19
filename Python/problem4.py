def ispalindrome(n): 
    tostring = str(n) 
    length = len(str(n)) 
    for i in range(0,int(length/2)): 
        if not tostring[i] == tostring[length-1-i]: 
            return False
    return True

def largest(n):
    big = [0,0,0]
    for x in range(1,n+1):
        for y in range(1,n+1):
            if ispalindrome(x*y) and x*y > big[0]:
                big = [x*y,x,y]
    return big


print(str(largest(999)))
