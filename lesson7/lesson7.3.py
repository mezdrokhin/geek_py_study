class Cell:
    number=0
    def __init__(self,n):
        self.number=n
    def __add__(self, other):
        return str(self.number+other.number)
    def __sub__(self, other):
        if self.number>other.number:
            return str(self.number-other.number)
        else:
            return 'Первое меньше второго, не хорошо...'
    def __mul__(self, other):
        return str(self.number*other.number)
    def __truediv__(self, other):
        return str(self.number//other.number)
    def make_order(self,leng):
        out=''
        rows=self.number//leng
        for i in range(rows):
            out=out+'*'*leng+'\n'
        out=out+'*'*(self.number%leng)
        return(out)
a=Cell(13)
b=Cell(7)
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a.make_order(3))