# На вход поступает список из вещественных чисел, записанных в строку через пробел. С помощью функции map преобразовать
# числа в строке в их вещественное представление и отобразить первые три числа. (Полагается,
# что минимум три вещественных числа имеются). Реализовать извлечение чисел через функцию next.
# Результат отобразить в строку через пробел.
# Sample Input:
# 4.35 -10.6 1.0 200.34 0.56
# Sample Output:
# 4.35 -10.6 1.0

def float_number(x):
    if x == float:
        yield x


a = map(float, input().split())
float_number(a)
for i in range(3):
    print(next(a), end=' ')