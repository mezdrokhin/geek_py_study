# Задание 1
print('Задание 1')
a=input('Введите число: ')
b=input('Введите текст: ')
print(a,b)

# Задание 2
print('Задание 2')
sec=int(input('Введите время в секундах: '))
h=sec//3600
m=(sec%3600)//60
s=sec-60*m-3600*h
print('Время в другом формате: {}:{}:{}'.format(h,m,s))

# Задание 3
print('Задание 3')
n=input('Введите число n: ')
result=int(n)+int(n*2)+int(n*3)
print('n + nn + nnn = {}'.format(result))

# Задание 4
print('Задание 4')
numb=input('Введите число: ')
l=[]
for i in numb:
    l.append(int(i))
print('Максимальная цифра: {}'.format(max(l)))

# Задание 5
print('Задание 5')
vir=int(input('Введите выручку: '))
izd=int(input('Введите издержки: '))
if izd > vir:
    print('Фирма отработала с убытком.')
else:
    print('Фирма отработала с прибылью. Рентабельность составила {}'.format((vir-izd)/vir))
    works=int(input('Введите число сотрудников: '))
    print('Прибыль на каждого сотрудника составила: {}'.format((vir-izd)/works))

# Задание 6
print('Задание 6')
aa=int(input('Введите результат в первый день: '))
bb=int(input('Введите требуемый результат: '))
km=aa
day=1
print('Результат')
print('1-й день: {}'.format(km))
while km<bb:
    km=km*1.1
    day=day+1
    print('{}-й день: {}'.format(day,km))
print('На {}-й день спортсмен достиг результата - не менее {} км'.format(day,bb))