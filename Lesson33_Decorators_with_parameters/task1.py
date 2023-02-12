# Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и
# возвращает их сумму.
# Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
# s = input()
# Результат отобразите на экране.
# Sample Input:
# 5 6 3 6 -4 6 -1
# Sample Output:
# 26

from functools import wraps


def dec_func(start):
    def func(func):
        @wraps(func)
        def wrapper(*args):
            res = start + func(*args)
            return res
        return wrapper
    return func


@dec_func(start=5)
def lst(x):
    """comment"""
    st = [int(i) for i in x.split()]
    return sum(st)


s = input()
print(lst(s))
print(lst.__name__)