# Декораторы функций с параметрами
# У нас получился декоратор дял вычисления производных произвольных функций
from functools import wraps  # это специальный декоратор, который встроен в Python
import math


def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):  # список фактических и формальных параметров.
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # wrapper.__name__ = func.__name__
        # wrapper.__doc__  = func.__doc__

        return wrapper
    return func_decorator


@df_decorator(dx=0.001)
def sin_df(x):
    """"Функция для вычисления производной синуса"""
    return math.sin(x)


print(sin_df.__name__)
print(sin_df.__doc__)