from time import time 
from time import sleep

def exp(n):
    return 10**n

def func():
    n = range(0,10)
    index = 0
    for a in n:
        for b in n:
            if not a == b:
                for c in n:
                    if not c in [a,b]:
                        for d in n:
                            if not d in [a,b,c]:
                                for e in n:
                                    if not e in [a,b,c,d]:
                                        for f in n:
                                            if not f in [a,b,c,d,e]:
                                                for g in n:
                                                    if not g in [a,b,c,d,e,f]:
                                                        for h in n:
                                                            if not h in [a,b,c,d,e,f,g]:
                                                                for i in n:
                                                                    if not i in [a,b,c,d,e,f,g,h]:
                                                                        for j in n:
                                                                            if not j in [a,b,c,d,e,f,g,h,i]:
                                                                                index += 1
                                                                                if index == 1000000:
                                                                                    result = 0
                                                                                    list = [a,b,c,d,e,f,g,h,i,j]
                                                                                    exponent = 9
                                                                                    for entry in list:
                                                                                        result = result + entry * exp(exponent)
                                                                                        exponent -= 1
                                                                                    return result
start = time()                                                                                
print(func())
print((time()-start))

from itertools import permutations
start = time()
herp = 0
exponent = 9
for i in list(permutations(range(10)))[10**6-1]:
    herp = herp + i*exp(exponent)
    exponent -= 1
print(herp)
print((time()-start))
