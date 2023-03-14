# Имеется таблица с данными, представленная в формате:
# Номер;Имя;Оценка;Зачет
# 1;Иванов;3;Да
# 2;Петров;2;Нет
# ...
# N;Балакирев;4;Да
# Эти данные необходимо представить в виде двумерного (вложенного) кортежа. Все числа должны быть представлены как целые
# числа. Затем, отсортировать данные так, чтобы столбцы шли в порядке:
# Имя;Зачет;Оценка;Номер
# Реализовать эту операцию с помощью сортировки.
# Результат должен быть представлен также в виде двумерного кортежа и присвоен переменной с именем t_sorted.
# Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# Номер;Имя;Оценка;Зачет
# 1;Портос;5;Да
# 2;Арамис;3;Да
# 3;Атос;4;Да
# 4;д'Артаньян;2;Нет
# 5;Балакирев;1;Нет
# Sample Output:
# True
lst_in = [
    "Номер;Имя;Оценка;Зачет",
    "1;Портос;5;Да",
    "2;Арамис;3;Да",
    "3;Атос;4;Да",
    "4;д'Артаньян;2;Нет",
    "5;Балакирев;1;Нет",
]
def func(list):
    # res = tuple((tuple(i.split(';'),)) for i in x)
    x = list.split(';')
    d = tuple()
    # for i in :
    if x[0].isdigit():
        d += x[1], x[3], int(x[2]), int(x[0])
    else:
        d += x[1], x[3], x[2], x[0]
    return d


t_sorted = tuple([tuple(func(i)) for i in lst_in])
print(t_sorted)


# another solution
def func2(x):
    order = {
        ind: "Имя;Зачёт;Оценка;Номер;".split(";").index(name)
        for ind, name in enumerate("Номер;Имя;Оценка;Зачёт".split(";"))
    }
    print(order)
    t_sorted = tuple(
        map(
            tuple,
            (
                sorted(
                    (int(i) if i.isdigit() else i for i in el.split(";")),
                    key=lambda x: order[el.split(";").index(str(x))],
                )
                for el in x
            ),
        )
    )
    return t_sorted


print(func2(lst_in))

# another solution


def func3(x):
    lst = []
    for ind, item in enumerate(x):
        num, name, asses, credit = item.split(";")
        temp = (
            [name, credit, asses, num]
            if (ind == 0)
            else [name, credit, int(asses), int(num)]
        )
        lst.append(tuple(temp))
    return tuple(lst)


t_sorted = func3(lst_in)
print(tuple(t_sorted))
