# Определите функцию с именем get_list_dig,
# которая возвращает список только из числовых значений переданной ей коллекции (список или кортеж).
# Сигнатура функции должна быть, следующей:
# def get_list_dig(lst): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.


def get_list_dig(lst) -> list:
    l = []
    for num in lst:
        if type(num) is int or type(num) is float:
            l.append(num)
    return l


print(get_list_dig((1, 2, 3, "a", True, [4, 5], "c", (4, 5))))


# another solution

def get_list_dig1(lst):
    return list(filter(lambda x: type(x) in (int, float), lst))

print(get_list_dig1((1, 2, 3, "a", True, [4, 5], "c", (4, 5))))