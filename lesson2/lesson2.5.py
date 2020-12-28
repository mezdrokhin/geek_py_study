my_list = [7, 5, 3, 3, 2]
new=input('Рейтинг сейчас {}, введите новый элемент: '.format(my_list))
my_list.append(int(new))
my_list.sort(reverse=True)
print(my_list)