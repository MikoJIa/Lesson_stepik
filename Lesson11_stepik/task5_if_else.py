# Вводятся четыре целых числа a, b, c, d в одну строку через пробел.
# Определить, войдет ли в конверт с внутренними размерами a и b мм прямоугольная открытка с размерами с и d мм.
# Для размещения открытки в конверте необходим зазор в 1 мм с каждой стороны. Открытку можно поворачивать на 90 градусов.
# Вывести ДА, если входит и НЕТ - если не входит.
# Sample Input:
# 12 5 7 2
# Sample Output:
# ДА

a, b, c, d = map(int, input().split())
if (a -1 > c) and (b - 1 > d) or (a - 1 > d) and (b - 1 > c):
    print('ДА')
else:
    print('НЕТ')
