import math

# abs() - это функция для вычислегия модуля числа, эта функция ысегда вызывается числовым аргументом

# print(abs(-5))
# # 5
# print(abs(1.5))
# # 1.5
# a = abs(-5.6)
# print(a)
# # 5.6
#
# # Функция min
# a = min(1, 2, 4, -5, 6, 8, 0)
# print(a)
#
# # Функция max
# b = max(1, 2, 4, 6, 78, 9)
# print(b)
#
# # Функция pow- возводит в сцепень которую задать
# a =pow(2, 4)
# print(a)
# b = pow(27, 1/3)
# print(b)
#
# a = max(1, 2, abs(-3), -10)
# print(a)
# c = max(1, 2, abs(min(10, 5, -3)), -10)
# print(c)
#
# # math.ceil возвращяет до наибольшего целого
# a = math.ceil(5.2)
# print(a)
# # math.floor округляет до наименьшего целого
# v = math.floor(-5.99)
# print(v)
# # math.factorial(6) 1*2*3*4*5*6
# z = math.factorial(6)
# print(z)
# # math.trunc отбрасывает дробную часть
# x = math.trunc(8.5)
# print(x)
# # math.sqrt вычисляет квадратный корень
# n = math.sqrt(49)
# print(n)

# Допишите текст программы для вычисления евклидового расстояния (гипотенузы) по перемещениям a и b.
# Округлите результат с точностью до сотых. Полученное значение выведите на экран.
# Пример: input 3 4
# output 5.0
#
# a, b = map(int, input('Введите два числа через пробел - ').split())
# c = math.sqrt(abs(pow(a, 2) + pow(b, 2)))
# print(round(c, 2))


def counts(data):
    s = []
    count = 0
    for i in range(len(data)-1):
        if data[i] >= count:
            s.append(data[i])
            count = data[i]
        else:
            s.append(count)

    return s


print(counts([5, 5, 6, 5, 5, 5, 5, 6]))
