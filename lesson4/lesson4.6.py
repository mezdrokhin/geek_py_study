import itertools

for el in itertools.count(3):
    if el > 10:
        break
    else:
        print(el)

с = 0
for el in itertools.cycle(['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you']):
    if с > 10000:
        break
    print(el)
    с += 1