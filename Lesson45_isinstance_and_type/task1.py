# Определите функцию с именем get_add, которая складывает или два числа или две строки (но не число со строкой) и
# возвращает полученный результат. Если сложение не может быть выполнено, то функция возвращает значение None.
# Сигнатура функции должна быть, следующей:
# def get_add(a, b): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.


def get_add(a, b):
    if type(a) in (float, int) and type(b) in (float, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    return None


print(get_add('1', 2))

# another solution

def add_numbers_and_string(a, b):
    if type(a) in (float, int) and type(b) in (float, int) or isinstance(a, str) and isinstance(b, str):
        return a + b


print(add_numbers_and_string(1, 2))