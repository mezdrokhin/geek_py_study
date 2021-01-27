class Zero(Exception):
    def __init__(self):
        print('Ноль нельзя!')

def delenie(a,m):
    try:
        if m==0:
            raise Zero
    except Zero:
        pass
    else:
        print(a/m)

a=10
m=0
delenie(a,m)
