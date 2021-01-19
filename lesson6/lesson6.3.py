class Worker:
    wage=0
    bonus=0
    income = {"wage": wage, "bonus": bonus}
    name=''
    surname=''
    position=''

class Position(Worker):
    def __init__(self,n,s,p,w,b):
        Worker.name=n
        Worker.surname=s
        Worker.position=p
        Worker.income["wage"]=w
        Worker.income["bonus"]=b
    def get_full_name(self):
        return Worker.name+' '+Worker.surname+' - '+Worker.position
    def get_total_income(self):
        return Worker.income["wage"]+Worker.income["bonus"]
a=Position('vasya','ivanov','boss',100,50)
print(a.get_full_name())
print(a.get_total_income())

# Не понимаю, как сделать защищенным income. Если я делаю везде __income, то вылазит ошибка, что нет Position.__income, то есть он не обращается к Worker, чтобы взять __income из него. Как нужно сделать? Из методички не врубился...