# Объявите функцию, которая принимает один аргумент (вещественное число), и возвращает квадрат этого числа.
# После объявления функции прочитайте (с помощью функции input) вещественное число и вызовите функцию с этим значением.
# Выведите на экран результат работы функции.
# Sample Input:
# 1.5
# Sample Output:
# 2.25

def sqrt(x):
    res = None if x < 0 else x ** 2
    return res


a = float(input())
print(sqrt(a))