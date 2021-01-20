class Worker:
    wage=0
    bonus=0
    __income = {"wage": wage, "bonus": bonus}
    name=''
    surname=''
    position=''
    def __init__(self, n, s, p, w, b):
        Worker.name = n
        Worker.surname = s
        Worker.position = p
        Worker.__income["wage"] = w
        Worker.__income["bonus"] = b

    def get_total_income(self):
        return self.__income["wage"] + self.__income["bonus"]

class Position(Worker):
    def __init__(self,n,s,p,w,b):
        Worker.__init__(self,n,s,p,w,b)
    def get_full_name(self):
        return Worker.name+' '+Worker.surname+' - '+Worker.position
    def get_total_income(self):
        return Worker.get_total_income(self)
a=Position('vasya','ivanov','boss',100,50)
print(a.get_full_name())
print('Полная зарплата: ',a.get_total_income())