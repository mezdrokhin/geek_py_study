import math
def fact(n):
    for el in range(1,n+1):
        yield math.factorial(el)

for el in fact(10):
    print(el)
