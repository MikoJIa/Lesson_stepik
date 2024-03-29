# Используя замыкания функций, объявите внутреннюю функцию, которая увеличивает значение своего аргумента на некоторую
# величину n - параметр внешней функции с сигнатурой:
# def counter_add(n): ...
# Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt.
# Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
# k = int(input())
# Выведите результат на экран.
# Sample Input:
# 5
# Sample Output:
# 7


def counter_add(n):
    def inner_func(x):
        return x + n
    return inner_func


k = int(input())
cmt = counter_add(2)
print(cmt(k))