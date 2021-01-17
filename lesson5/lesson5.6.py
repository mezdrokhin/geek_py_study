with open("file6.txt", 'r', encoding='utf-8') as f6:
    content = f6.readlines()
d1={}
for el in content:
    el1=el.split(': ')
    values=el1[1].split(' ')
    symlist=[]
    for el2 in values:
        symbols=el2.split('(')
        for ss in symbols:
            symlist.append(ss)
    result=0
    for el4 in symlist:
        if el4.isdigit():
            result=result+int(el4)
    d1[el1[0]]=result
print(d1)