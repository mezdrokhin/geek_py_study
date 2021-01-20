class Car:
    speed=0
    color=''
    name=''
    is_police=False
    def __init__(self,speed,color,name):
        self.speed = speed
        self.color = color
        self.name = name
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self,direction):
        print('Машина повернула',direction)
    def show_speed(self):
        print('Скорость ', self.speed)
class TownCar(Car):
    def __init__(self,speed, color, name):
        Car.__init__(self,speed, color, name)
        self.is_police = False
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print('Превышение!!!')
class SportCar(Car):
    def __init__(self,speed, color, name):
        Car.__init__(self,speed, color, name)
        self.is_police = False
class WorkCar(Car):
    def __init__(self,speed, color, name):
        Car.__init__(self,speed, color, name)
        self.is_police = False
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print('Превышение!!!')
class PoliceCar(Car):
    def __init__(self,speed, color, name):
        Car.__init__(self,speed, color, name)
        self.is_police = True
a=TownCar(100,'red','Девятка')
b=WorkCar(30,'blue','Бетономешалка')
c=SportCar(200,'yellow','Ламбо')
d=PoliceCar(150,'white','Бобик')
l=[a,b,c,d]
for el in l:
    print('Машина: ',el.speed,el.color,el.name,el.is_police)
    el.go()
    el.stop()
    el.turn('Налево')
    el.show_speed()
