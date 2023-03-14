# Определите функцию с именем get_even_sum, которая принимает на входе итерируемый объект
# (список, строку, кортеж, словарь, множество) и вычисляет сумму только целых четных чисел,
# взятых из элементов итерируемого объекта. Результат возвращается функцией. Если целых чисел нет, то возвращается 0.
# Сигнатура функции должна быть, следующей:
# def get_even_sum(it): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.


def get_even_sum(it: (list, str, tuple, dict, set)) -> int:
    total = 0
    for num in it:
        if type(num) is (list, tuple, dict) and num % 2 == 0:
            total += get_even_sum(num)
        if type(num) == int and num % 2 == 0:
            total += num
    return total


print(get_even_sum({5, 6, 7, '8', 5, '4'}))

# another solution

def get_even_sum1(it) -> int:
    total = 0
    for num in it:
        if type(num) is (int) and num % 2 == 0:
            total += num
    return total


print(get_even_sum1({5, 6, 7, '8', 5, '4'}))