class Road:
    _length=0
    _width=0
    def __init__(self,p1,p2):
        Road._length=p1
        Road._width=p2
    def mass(self,plotnost,height):
        return Road._width*Road._length*plotnost*height
a=Road(20,5000)
print(a.mass(25,5))