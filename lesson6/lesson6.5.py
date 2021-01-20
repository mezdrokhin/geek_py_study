class Stationery:
    title=''
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка карандашом')
        self.title = 'Карандаш'
class Pencil(Stationery):
    def draw(self):
        print('Отрисовка ручкой')
        self.title = 'Ручка'
class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')
        self.title = 'Маркер'
a=Pen()
b=Pencil()
c=Handle()
a.draw()
print(a.title)
b.draw()
print(b.title)
c.draw()
print(c.title)

