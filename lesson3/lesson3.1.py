def delenie(a1,a2):
    return a1/a2
b1=int(input('Введите делимое: '))
b2=int(input('Введите делитель: '))

try:
    print('Ответ: ', delenie(b1,b2))
except ZeroDivisionError:
    print('Дружочек, на ноль делить нельзя...')