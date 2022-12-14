d = {'house': 'Дом', 'car': 'машина',
     'tree': 'дерево',
     'road': 'дорога', 'river': 'река'}
print(d)
print(d['house']) # Дом
print(d['river']) # река
# Мы можем создавать словари с помощью такой функции как dict()
s = dict(one=1, two=2, tree='3', four='4')
print(s)
# Как изменить вложеный список в словарь
lst = [[2, 'неудовлетворительно'],[3, 'удовлетворительно'],[4, 'хорошо'], [5, 'отлично']]
n = dict(lst) # {2: 'неудовлетворительно', 3: 'удовлетворительно', 4: 'хорошо', 5: 'отлично'}
print(n)

c = {}
c[True] = 'Истина'
print(c) # {True: 'Истина'}
c[False] = 'Ложь'
print(c) # {True: 'Истина', False: 'Ложь'}
# Ключи могут быть только неизменяемые значения, а вот сами значения могут быть любые
d = {True: 1, False: 'Ложь', 'List': [1, 2, 3, 4], 5: 5}
print(d)
# Если мы хотим определить число элементов в словаре то это len()
print(len(d)) # 4
# Если необходимо удалить ключь-значение то это del
del d[True]
print(d) # {False: 'Ложь', 'List': [1, 2, 3, 4], 5: 5}
# Если мы хотим проверить есть ли ключ в словаре мы используем in
print('abc' in d) # False
# Обратная проверка ключа которого нет not in
print('Ложь' not in d) # True


print(d)