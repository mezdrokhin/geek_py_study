str_list = ['Иванов 10000\n', 'Петров 15000\n', 'Сидоров 40000\n']
with open("file3.txt", 'w') as f3:
    f3.writelines(str_list)
with open("file3.txt", 'r') as f3:
    content = f3.readlines()
    salary=[]
for el in content:
    person=el.split(' ')
    salary.append(int(person[1]))
    if int(person[1])<20000:
        print(person[0])
print('Средняя зп: ',sum(salary)/len(salary))