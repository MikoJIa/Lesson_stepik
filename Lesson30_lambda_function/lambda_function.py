# Анонимная функция или как подругому её называют: Лямбда функция!
print(lambda a, b: a + b)
# Что бы вызвать функцию лямбда, её геобходимо присвоить переменной
s = lambda a, b: a + b
print(s(1, 2))
# Создадим список и функцию в нутри списка, и вызовим функцию лямбда
lst = [4, 5, lambda: print('lambda'), 7, 8]
print(lst[2]())
# У нас есть список. Мы хотим, что-бы наша функция вызывала элемент по определённому критерию.
ls = [5, 3, 0, -6, 8, 10, 1]


def get_filter(a, filter=None):
    if filter is None:
        return ls

    res = []
    for x in a:
        if filter(x):
            res.append(x)
    return res


r = get_filter(ls, lambda x: x % 2 == 0)
print(r)  # [0, -6, 8, 10]

