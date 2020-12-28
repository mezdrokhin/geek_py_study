decision='Да'
numb=1
goods=[]
while decision=='Да' or decision=='ДA'or decision=='да':
    name=input('Введите название {} товара: '.format(numb))
    price=int(input('Введите цену {} товара: '.format(numb)))
    quan=int(input('Введите количество {} товара: '.format(numb)))
    ed=input('Введите единицы измерения {} товара: '.format(numb))
    good=(numb, {"название":name},{"цена":price},{"количество":quan},{"ед":ed})
    numb=numb+1
    decision = input('Еще товар? Да или Нет: ')
    goods.append(good)
print(goods)

#  тестовые данные
# goods=[(1, {'название': 'компьютер'}, {'цена': 12}, {'количество': 13}, {'ед': 'шт'}), (2, {'название': 'мыло'}, {'цена': 1232}, {'количество': 345}, {'ед': 'литры'})]
# print(goods)
# print(type(goods))
# print(type(goods[0][1].keys()))
# print(goods[0][2].values())
# print(len(goods))
# print(goods[0][2]['цена'])

# блок аналитики
anal={"название":[],"цена":[],"количество":[],"ед":[]}
for i in range(len(goods)):
    anal["название"].append(goods[i][1]['название'])
    anal["цена"].append(goods[i][2]['цена'])
    anal["количество"].append(goods[i][3]['количество'])
    anal["ед"].append(goods[i][4]['ед'])
print('Аналитика по товарам: {}'.format(anal))

