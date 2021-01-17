with open("my_file.txt", 'w') as f_1:
    data ='.'
    while data !='':
        data=input('vvedite stroky: ')
        f_1.write(data)
        f_1.write('\n')