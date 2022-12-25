# Метод словаря dict.fromkeys(список[, значение по умолчанию])
lst = ['+1', '+2', '+3', '+4']
a = dict.fromkeys(lst)
print(a) # {'1': None, '2': None, '3': None, '4': None}
a = dict.fromkeys(lst, 'cod country')
print(a) # {'+1': 'cod country', '+2': 'cod country', '+3': 'cod country', '+4': 'cod country'}
a.clear()
print(a) # {}
d = {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
print(d) # {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
# Создадим копию словаря
d2 = d.copy()
print(d2) # {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
d2['list'] = [5, 6, 7]
print(d2) # {True: 1, False: 'Ложь', 'list': [5, 6, 7], 5: 5}
print(d) # {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
# Ещё один метод созданя копии - это dict()
d2 = dict(d)
print(d2) # {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
# Получить значение словаря с помощью функции get()
print(d.get('list')) # [1, 2, 3]
# Чем же отличается функция get() от d[ключ], тем что функция get() будет возвращать None если ключа в словаре нет как можно
# этим воспользоватся
# Например:
print(d.get(3)) # None
print(d.get(3, False)) # False
# То есть мы проверяем, если ключа 3 нету в словаре мы возврашаем False!!!
# Следующий метод dict.setdefault(key[, default]) тоже возвращает значение по заданному ключу, но если ключа в словаре
# нет то setdefault() сохраняет в словаре этот ключ которого там небыло
print(d.setdefault(3)) # None
print(d) # {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5, 3: None}
# Удалим клю 3
del d[3]
print(d) # {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
# Если ключа не существует в словаре мы просто возвращаем значение и ключь в словарь
d.setdefault(3, 'three')
print(d) # {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5, 3: 'three'}
# метод pop() удаление ключа
d.pop(3)
print(d) # {True: 1, False: 'Ложь', 'list': [1, 2, 3], 5: 5}
# Метод pop() удаляет и возвращает тот элемен который удалил, воспользуемся этим если ключа в словаре нет
print(d.pop(3, False)) # False
# Метод popitem(удаляет случайно выбранный ключ)
print(d.popitem()) # (5, 5)
print(d) # {True: 1, False: 'Ложь', 'list': [1, 2, 3]}
# Метод keys() возвращает список ключей
print(d.keys()) # dict_keys([True, False, 'list'])
print(d)                  # {True: 1, False: 'Ложь', 'list': [1, 2, 3]}
# Метод значения values()
print(d.values()) # dict_values([1, 'Ложь', [1, 2, 3]])
print(d)                # {True: 1, False: 'Ложь', 'list': [1, 2, 3]}
for x in d.values():
    print(x) # 1 Ложь [1, 2, 3]
# А еслт мы хотим взять из словаря и ключи и значения, воспользуемся методом items()
for i in d.items():
    print(i) # (True, 1) (False, 'Ложь') ('list', [1, 2, 3]) i будет у нас уже являтся кортежом(tuple)
for key, value in d.items():
    print(key, value) # True 1 False Ложь list [1, 2, 3]
# Слияние двух словарей, создадим два словаря
f = dict(one = 1, two = 2, three = 3, four = 4)
print(f) # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
g = {2: 'неудовлетворительно', 3: 'удовлетворительно', 'four': 'хорошо', 5: 'отлично'}
print(g)
f.update(g)
print(f)
f = dict(one = 1, two = 2, three = 3, four = 4)
print(f)
print(g)
# объеденить два словаря
d3 = {**f, **g}
print(d3) # {'one': 1, 'two': 2, 'three': 3, 'four': 'хорошо', 2: 'неудовлетворительно', 3: 'удовлетворительно', 5: 'отлично'}
# поменяем порядок записи объединения
d3 = {**g, **f}
print(d3) # {2: 'неудовлетворительно', 3: 'удовлетворительно', 'four': 4, 5: 'отлично', 'one': 1, 'two': 2, 'three': 3}
# Ещё два и более словаря можно объединить вот такой записью
print(g | f) # {2: 'неудовлетворительно', 3: 'удовлетворительно', 'four': 4, 5: 'отлично', 'one': 1, 'two': 2, 'three': 3}