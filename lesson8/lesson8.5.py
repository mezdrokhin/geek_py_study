class Complex:
    i=0
    j=0
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def __add__(self, other):
        return [self.i+other.i,self.j+other.j]
    def __str__(self):
        return str([self.i,self.j])
    def __mul__(self, other):
        return [self.i*other.i-self.j*other.j,self.i*other.j+self.j*other.i]

a=Complex(1,1)
b=Complex(2,4)
print(a+b)
print(a)
print(a*b)