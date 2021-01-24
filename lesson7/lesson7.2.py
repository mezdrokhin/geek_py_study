import abc
class ClothesAbstractClass(abc.ABC):
    @abc.abstractmethod
    def square(self):
        pass
class Coat(ClothesAbstractClass):
    def __init__(self,parameter):
        self.parameter=parameter
    @property
    def square(self):
        return self.parameter / 6.5 + 0.5

class Costume(ClothesAbstractClass):
    def __init__(self,parameter):
        self.parameter=parameter
    @property
    def square(self):
        return 2 * self.parameter + 0.3
a=Coat(100)
b=Costume(200)
c=Coat(150)
d=Costume(300)
print(a.square+b.square+c.square+d.square)