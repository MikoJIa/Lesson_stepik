# Объявите анонимную (лямбда) функцию для вычисления модуля числа (то есть, отрицательные числа нужно делать
# положительными). Вызовите эту функцию для введенного числа x:
# x = float(input())
# Отобразите результат работы функции на экране.
# Sample Input:
# -5.6
# Sample Output:
# 5.6

x = float(input())
res = lambda a: abs(a)
print(res(x))

# another solution математическим путём

x = float(input())
get_div = lambda x: (x**2)**0.5
print(get_div(x))