#Вариант через лист
monthlist=['winter','winter','spring','spring','spring','summer','summer','summer','autumn','autumn','autumn','winter']
print(monthlist[int(input('Введите номер месяца: '))-1])

#Вариант через словарь
monthdict= {1:'winter',2:'winter',3:'spring',4:'spring',5:'spring',6:'summer',7:'summer',8:'summer',9:'autumn',10:'autumn',11:'autumn',12:'winter'}
print(monthdict.get(int(input('Введите номер месяца: '))))
