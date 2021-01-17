with open("file2.txt", 'w') as f2:
    str_list = ['stroka_1 stroka_1_slovo2 slovo3\n', 'stroka_2 slovo2\n', 'stroka_3\n']
    f2.writelines(str_list)
with open("file2.txt", 'r') as f2:
    content=f2.readlines()
    print('Число строк: ', len(content))
    print('Число слов в строках: ')
    for el in content:
        words=el.split(' ')
        print(len(words))