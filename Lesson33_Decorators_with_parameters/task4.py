# Объявите функцию с именем get_list и следующим описанием в теле функции:
# '''Функция для формирования списка целых значений'''
# Сама функция должна формировать и возвращать список целых чисел, который поступает на ее вход в виде строки из целых
# чисел, записанных через пробел.
# Определите декоратор, который выполняет суммирование значений из списка этой функции и возвращает результат.
# Внутри декоратора декорируйте переданную функцию get_list с помощью команды @wraps
# (не забудьте сделать импорт: from functools import wraps). Такое декорирование необходимо,
# чтобы исходная функция get_list сохраняла свои локальные свойства: __name__ и __doc__.
# Примените декоратор к функции get_list, но не вызывайте ее.

from functools import wraps


def dec_func():
    def decor(func):
        @wraps(func)
        def wrapper(*args):
            res = func(*args)
            return sum(res)
        return wrapper
    return decor


@dec_func()
def get_list(a):
    """Функция для формирования списка целых значений"""
    res = [int(i) for i in a.split()]
    return res


st = input()
print(get_list(st))


# another solution

def deco_sum(a):
    @wraps(a)
    def wrapper(*args):
        return sum(a(*args))
    return wrapper

@deco_sum
def get_list(s):
    res = [int(i) for i in s.split()]
    return res


s = input()
print(get_list(s))