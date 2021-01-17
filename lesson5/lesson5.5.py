str=('324 6 4 5 7 3 35 6 5434 5 6')
with open("file5.txt", 'w') as f5:
    f5.write(str)
with open("file5.txt", 'r') as f5:
    content = f5.read()
new=content.split(' ')
newint=map(int,new)
print('summa = ', sum(newint))