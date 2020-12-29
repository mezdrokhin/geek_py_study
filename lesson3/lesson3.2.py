def user(name,soname,year,city,mail,tel):
    print('Пользователь {} {}, {} года рождения из города {}. Контакты: почта {}, телефон {}'.format(name,soname,year,city,mail,tel))
n=input('Введите имя: ')
s=input('Введите фамилию: ')
y=input('Введите год рождения: ')
c=input('Введите город: ')
m=input('Введите электронную почту: ')
t=input('Введите телефон: ')
user(soname=s,name=n,city=c,mail=m,year=y,tel=t)