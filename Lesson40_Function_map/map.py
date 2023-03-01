#
b = map(int, ['1', '2', '3', '5', '7'])  # дважды проитись по этой коллекции нельзя генератор сработает только раз
# или можно записать иначе
b1 = (int(x) for x in ['1', '2', '3', '5', '7'])
a = sum(list(b))
print(a)

cities = ['Минск', 'Борисов', 'Брест', 'Могилёв', 'Гомель']
length_city = map(len, cities)
# for i in length_city:
#     print(i, end=' ')
# или записать можно вот так
a = list(length_city)
print(a)

up_city = map(str.upper, cities)
c = list(up_city)
print(c)
v = map(lambda x: x[::-1], c)
n = list(v)
print(n)
