def my_func(x,y):
    print('Первый способ',x**y)
    res=1
    for i in range(abs(y)):
        res=res*x
    print('Второй способ', res) if y>0 else print('Второй способ', 1/res)
x=5
y=-3
my_func(x,y)