res=0
l=[]
br='!'
do=True
while do:
    l=input('Вводите числа через пробел, когда надоест напишите в конце восклицательный знак: ')
    print(l)
    if l[-1]==' ': #проверка - если последним ввели пробел, а не число
        print(l[-1])
        l=l[0:(len(l)-1)]
    if br in l:
        do=False
    lnew=l.split(' ')
    for i in range(len(lnew)):
        if (lnew[i] !='!'):
            res=res+int(lnew[i])
    print('Сумма введенных чисел: ', res)
