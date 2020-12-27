l=input('Введите строку: ')
#l='Привет я хочу питсу и самбитибургер'
lnew=l.split(' ')
n=1
for i in lnew:
    if len(i)>10:
        print(n,' ',i[0:10])
    else:
        print(n, ' ', i)
    n=n+1
