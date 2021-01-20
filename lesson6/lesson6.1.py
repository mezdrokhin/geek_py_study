import time
class TrafficLight:
    __trafficlight_color=''
    def running(self):
        TrafficLight.__trafficlight_color='red'
        print('Горит красный')
        time.sleep(1)
        TrafficLight.__trafficlight_color = 'yellow'
        print('Горит желтый')
        time.sleep(2)
        TrafficLight.__trafficlight_color = 'green'
        print('Горит зеленый')
        time.sleep(3)
a=TrafficLight()
a.running()