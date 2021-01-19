class Car:
    speed=0
    color=''
    name=''
    is_police=False
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self,direction):
        print('Машина поехала ', direction)
    def show_speed(self,speed):
        print('Скорость ', speed)
class TownCar(Car):
    def __init__(self,speed, color, name):
        super().__init__(speed,color,name)
        Car.speed=speed
        Car.color=color
        Car.name=name
        Car.is_police = False
    def show_speed(self,speed):
        super().show_speed(is_police,speed)
        limit=''
        if speed > 60:
            limit='Превышение!!!'
        print('Скорость Таун Кара ',speed, limit)
class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police)
        Car.speed = s
        Car.color = c
        Car.name = n
        Car.is_police = True
    def show_speed(self,speed):
        super().show_speed(is_police, speed)
        if speed > 40:
            limit='Превышение!!!'
        print('Скорость Рабочей Машины ',speed, limit)
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police)
        Car.speed = s
        Car.color = c
        Car.name = n
        Car.is_police = True
    def show_speed(self,speed):
        super().show_speed(is_police, speed)
        print('Скорость Рабочей Машины ',speed)
class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police)
        Car.speed = s
        Car.color = c
        Car.name = n
        Car.is_police = False
    def show_speed(self,speed):
        super().show_speed(is_police, speed)
        print('Скорость Рабочей Машины ',speed)
a=TownCar(100,'red','Девятка')
b=WorkCar(30,'blue','Бетономешалка')
c=SportCar(200,'yellow','Ламбо')
d=PoliceCar(150,'white','Бобик')
l=[a,b,c,d]
for el in l:
    print('Машина: ',el.show_speed(),el.color,el.name,el.is_police)
    el.go()
    el.stop()
    el.turn('Налево')
