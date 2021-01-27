class Valid(Exception):
    pass
class Warehouse:
    dep1={"printers":{"number":0},"scaners":{"number":0}}
    dep2={"printers":{"number":0},"scaners":{"number":0}}
class Tech:
    def __init__(self,size,price):
        self.size=size
        self.price=price
        pass
class Printer(Tech):
    param1=0
    def __init__(self,size,price,dep,param1):
        super().__init__(size,price)
        self.param1=param1
        if dep=='dep1':
            Warehouse.dep1["printers"]["number"]=Warehouse.dep1["printers"]["number"]+1
            new='printer_'+str(Warehouse.dep1["printers"]["number"])
            Warehouse.dep1["printers"][new]={"size":size,"price":price,"param1":param1}
        if dep=='dep2':
            Warehouse.dep2["printers"]["number"]=Warehouse.dep2["printers"]["number"]+1
            new='printer_'+str(Warehouse.dep2["printers"]["number"])
            Warehouse.dep2["printers"][new]={"size":size,"price":price,"param1":param1}
class Scaner(Tech):
    param2=0
    def __init__(self,size,price,dep,param2):
        super().__init__(size,price)
        self.param2=param2
        if dep=='dep1':
            Warehouse.dep1["scaners"]["number"]=Warehouse.dep1["scaners"]["number"]+1
            new='scaner_'+str(Warehouse.dep1["scaners"]["number"])
            Warehouse.dep1["scaners"][new]={"size":size,"price":price,"param2":param2}
        if dep=='dep2':
            Warehouse.dep2["scaners"]["number"]=Warehouse.dep2["scaners"]["number"]+1
            new='scaner_'+str(Warehouse.dep2["scaners"]["number"])
            Warehouse.dep2["scaners"][new]={"size":size,"price":price,"param2":param2}
a=Printer(10,100,'dep1','A')
b=Printer(11,110,'dep1','B')
c=Scaner(12,120,'dep1','C')
d=Scaner(13,130,'dep2','D')

type=input('Введите тип техники ( Printer или Scaner ): ')

def sizeinput():
    try:
        size=input('Введите размер техники: ')
        if size.isdigit()!=True:
            raise Valid
    except Valid:
        print('Нужно ввести число!')
        return None
    else:
        return size


def priceinput():
    try:
        price=input('Введите стоимость техники: ')
        if price.isdigit()!=True:
            raise Valid
    except Valid:
        print('Нужно ввести число!')
        return None
    else:
        return price

size=None
while size==None:
    size=sizeinput()
price=None
while price==None:
    price=priceinput()
dep=input('Введите департамент, куда идёт техника ( dep1 или dep2 ): ')
if type=='Printer':
    param1=input('Введите параметр принтера ( A или B ): ')
    e=Printer(size,price,dep,param1)
if type=='Scaner':
    param2=input('Введите параметр сканера ( C или D ): ')
    e=Scaner(size,price,dep,param2)

print('Техника департамента 1: ', Warehouse.dep1)
print('Техника департамента 2: ', Warehouse.dep2)