import functools
def my_func(a1,a2):
    return a1*a2
g=[l for l in range(100, 1001) if l%2==0]
print(functools.reduce(my_func, g))