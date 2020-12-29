def my_funk(a1,a2,a3):
    l=[a1,a2,a3]
    m=min(l)
    for i in range(len(l)):
        if l[i]==m:
            n=i
    del l[n]
    print('Сумма двух наибольших чисел: ', sum(l))
a1=int(input('Введите первое число: '))
a2=int(input('Введите второе число: '))
a3=int(input('Введите третье число: '))
my_funk(a1,a2,a3)