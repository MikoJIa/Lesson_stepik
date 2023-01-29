# Как работают операторы * и **
# Мы знаем что *args - кортеж из элементов а **kwargs - это словарь из именованных переменных
x, c = (1, 2)
print(x)  # 1
print(c)  # 2
x, *c = (1, 2, 3, 4, 4, 5)
print(x)  # 1
print(c)  # [2, 3, 4, 4, 5]
# или наоборот
*x, c = (1, 2, 3, 4, 4, 5)
print(x)  # [1, 2, 3, 4, 4]
print(c)  # 5
# мы можем это использовать только для итерируемых объектов
x, *c = [1, 'a', True, 4]
print(x)  # 1
print(c)  # ['a', True, 4]
*x, c, z = 'Hello Python!'
print(x)  # ['H', 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o']
print(c)  # n
print(z)  # !
# Но мы не можем упаковать уже упакованые элементы
# *x = 1, 2, 3
# print(x)  # SyntaxError: starred assignment target must be in a list or tuple
# Всё по тому что 1,2,3 уже представляет кортеж, мы не можем упаковать уже упакованный кортеж
# а вот распаковать можем
*x, c = 1, 2, 3
print(x)  # [1, 2]
print(c)  # 3
# А как же нам распаковать например список
a = [1, 2, 3]
print(*a,)  # 1 2 3

d = -5, 5
print(d)  # (-5, 5)
# если мы вызовем в функции range() просто d то получим ошибку, а вот если мы распакуем range(*d) ошибки не будет
print(range(*d))  # range(-5, 5)
print(list(range(*d)))  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
# вот если мы запишем данным образом у нас получится автоматическая распаковка данных
print([range(*d)])  # [range(-5, 5)]
# у нас произойдёт распаковка значения в функции range()
print([*range(*d)])  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
# Мы можем распаковать несколько объктов в список
print([*range(*d), *(True, False), *a])  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, True, False, 1, 2, 3]
# Тоже-самое мы можем сделать со словарём
d = {0: 'безнадёжно', 1: 'убого', 2: 'неуд.', 3: 'удовл.', 4: 'хорошо', 5: 'отлично'}
# если мы сделаем вот так: {*d} то на выходе получим множества всё по тому-что * перебирает итерируемые объекты
print({*d})  # {0, 1, 2, 3, 4, 5}
# а можем сделать вот так: {*d.values()} и тогда мы получим множества из значений словаря
print({*d.values()})  # {'безнадёжно', 'удовл.', 'неуд.', 'убого', 'хорошо', 'отлично'}
# А если указать {*d.items()} то мы получим множества из кортежей
print({*d.items()})  # {(3, 'удовл.'), (4, 'хорошо'), (2, 'неуд.'), (1, 'убого'), (0, 'безнадёжно'), (5, 'отлично')}
# А если требуется распаковать словарь как словарь тогда надо поставить две **
print({**d})  # {0: 'безнадёжно', 1: 'убого', 2: 'неуд.', 3: 'удовл.', 4: 'хорошо', 5: 'отлично'}
# а что если у нас есть второй словарь и мы хотели бы их объединить?! Промто нужно распаковать два словаря
d2 = {6: 'превосходно', 7: 'элитарно', 8: 'божественно'}
print({**d, **d2})  # {0: 'безнадёжно', 1: 'убого', 2: 'неуд.', 3: 'удовл.', 4: 'хорошо', 5: 'отлично', 6: 'превосходно'
# , 7: 'элитарно', 8: 'божественно'}
# распаковка ключей словаря в переменные
a, b, *c = d
print(a)  # 0
print(b)  # 1
print(c)  # [2, 3, 4, 5]