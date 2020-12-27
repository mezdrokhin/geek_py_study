print('задание 2')
l=[]
new='1'
while new !='':
    new=input('vvedite chislo ')
    if new !='': # если просто нажать энтер, то ввод прекратится
        l.append(new)
print(l)
newl=[]
if len(l)%2==0:
    for i in range(len(l)):
        if i%2==0:
            newl.append(l[i+1])
        elif i%2!=0:
            newl.append(l[i-1])
elif len(l)%2!=0:
    for i in range(len(l)-1):
        if i%2==0:
            newl.append(l[i+1])
        elif i%2!=0:
            newl.append(l[i-1])
    newl.append(l[len(l)-1])
print(newl)