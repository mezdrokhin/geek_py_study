class Control(Exception):
    def __init__(self):
        print('Вводите только числа!')

data=''
datalist=[]
while data!='stop':
    try:
        data=input('Введите число')
        if data.isdigit()==False:
            raise Control
        datalist.append(data)
    except Control:
        pass
print(datalist)