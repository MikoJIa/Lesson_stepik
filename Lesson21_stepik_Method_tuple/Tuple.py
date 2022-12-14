# Кортежи - это упорядоченая, но не изменяемая колекция произвольных данных
# как создать кортеж из одного элемента
a = (1,)
print(a)  # (1,)
# или
b = 2,
print(b)  # (2,)
x, m = 1, 2
print(x)  # 1
print(m)  # 2
a, b = 'ra'
print(a)  # r
print(b)  # a
# мы создали ключ для словаря из данных кортежа
a = 1, 2, 3
d = {}
d[a] = 'кортеж'
print(d)
# еще очень важно то, что кортеж в отличии от списка занимает меньше места в памяти
lst = [1, 2, 3]
print(lst.__sizeof__())  # 104
print(a.__sizeof__())  # 48
# создание пустого кортежа
s = ()
v = tuple()
print(s)  # ()
print(v)  # ()
# влаживаем элементы с одного кортежа в другой
s = s + (1,)
print(s)  # (1,)
s = s + a
print(s)  # (1, 1, 2, 3)
a = a + s
print(a)  # (1, 2, 3, 1, 1, 2, 3)
#
b = (1, 2) * 10
print(b)
a = tuple([1, 2, 3])
print(a)  # (1, 2, 3)
a = tuple('hello')
print(a)  # ('h', 'e', 'l', 'l', 'o')
# кортеж перевести в список
t = 1, 2, 3
t = list(t)
print(t)  # [1, 2, 3]
# кортеж из разных элементов
a = (True, [1, 2, 3], 'hello', 5, {'house': 'дом'})
# обратимся по индексу
print(a[1])  # [1, 2, 3]
#  в этом кортеже имеется список, мы теперь в этое список добавим элемент
a[1].append('5')
print(a) # (True, [1, 2, 3, '5'], 'hello', 5, {'house': 'дом'})
# tuple.count(значение) - возвращает число найденых элементов с указанным значением;
w = ('abc', 2, [1, 2], True, 2, 5)
print(w.count('abc')) # 1
print(w.count(2)) # 2

# tuple.index(значение,[start,[stop]]) - возвращает индекс первого найденого элемента с указаным значением(start, stop)
# не обязательные параметры, индексы начала и конца поиска.
print(w.index(2, 2)) # 4 найденая двоечка под индексом 4
print(w.index(2, 2, 5)) # 4
# in
print(3 in w) # False нет такого элемента в данном кортеже
print([1, 2] in w) # True
d = (False,)
print(type(d))