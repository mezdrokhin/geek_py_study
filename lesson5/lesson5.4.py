with open('file4a.txt', 'r') as f4a:
    content=f4a.readlines()
new=[]
for el in content:
    st=el.split(' ')
    if st[0] =='One':
        new.append('Один'+' — '+st[2])
    if st[0] =='Two':
        new.append('Два'+' — '+st[2])
    if st[0] =='Three':
        new.append('Три'+' — '+st[2])
    if st[0] =='Four':
        new.append('Четыре'+' — '+st[2])
with open('file4b.txt', 'w', encoding='utf-8') as f4b:
    f4b.writelines(new)