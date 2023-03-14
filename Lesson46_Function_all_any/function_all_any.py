# Принимают ли все элементы списка значение True
# Функция all возвращает нам True, если все элементы списка или любого итерируемого объкта который мы передаём принимает
# значение True
a = [True, True, True, True]
# если все значения в списке True, переменная 'а' вернёт True
b = all(a)
print(b)  # True
# А если хотя бы один элемент будет = False, то программа нам вернёт False
a = [True, False, True, True]
b = all(a)
print(b)  # False
# А что делать если у нас список с разными значениями??1!!

a = [0, 1, 2.5, '', 'Python', [], [1, 2], {}]
# Все значения этого списка получают значение bool, если все значения списка принимают значение True функция вернёт нам
# True, а если хоть один элемент получает значение False, то функция вернёт False
b = all(a)
print(b)  # False
# For example:
a = [1, 2, 3.5, 'Python', [1, 2]]
b = all(a)
print(b)  # True

a = [1, 2, 3.5, 'Python', [1, 2]]
all_res = True
for x in a:
    all_res = all_res and bool(x)
print(all_res)  # True если все операнды True

a = [0, 1, 2, 3.5, 'Python', [1, 2]]
all_res = True
for x in a:
    all_res = all_res and bool(x)
print(all_res)  # False одтн операнд у нас False 0
#     Function any() - будет истина если хотя бы одно значение в списке истина
#     Function any() - вернёт ложь в том случае если все элементы ложь, если хоть один элемент будет являться истиной то
#     функция возвратит истину
a = [0, 1, 2, 3.5, 'Python', [1, 2]]
print(any(a))  # True
b = [0, [], {}, False]
print(any(b))  # False

a = [0, 1, 2, 3.5, 'Python', [1, 2]]
all_res = False
for x in a:
    all_res = all_res or bool(x)
print(all_res)  # True

                                #Теперь мы попробуем эти функции применить!!!!
                                #Игра крестики нолики
def true_for_x(a: str) -> bool:
    return a == 'x'


p = ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
row_1 = all(map(true_for_x, p[:3]))
row_2 = all(map(true_for_x, p[3:6]))
row_3 = all(map(true_for_x, p[6:9]))
# проверка по столбцам
col_1 = all(map(true_for_x, p[::3]))
col_2 = all(map(true_for_x, p[1::3]))
col_3 = all(map(true_for_x, p[2::3]))

dig_1 = all(map(true_for_x, p[0::4]))
dig_2 = all(map(true_for_x, p[2::2]))

print(row_1, row_2, row_3)  # False False True
print(col_1, col_2, col_3)  # False True False
print(dig_1, dig_2)  # True False
                                                # Игра сопёр
# поле юудет состоять размером NxN
n = 10
p = [0] * (n*n)
# где-то на поле с индексом 4 будет распологатся мина - *
p[4] = '*'
# если на поле появится этот знак - '*', значет пользователь наступил на мину и он проиграл
loss = any(map(lambda x: x == '*', p))
print(loss)
