# На вход программы подается вещественное число. Необходимо импортировать только одну функцию floor из модуля math,
# вызывать ее для введенного числа и отобразить результат на экране.
# Sample Input:
# 8.11
# Sample Output:
# 8
from math import floor as floo


def func_floor(x):
    return floo(x)


print(func_floor(float(input())))

