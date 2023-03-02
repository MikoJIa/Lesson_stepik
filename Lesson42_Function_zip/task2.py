# Вводится неравномерная таблица целых чисел. С помощью функции zip выровнить эту таблицу, приведя ее к прямоугольному
# виду, отбросив выходящие элементы. Вывести результат на экран в виде такой же таблицы чисел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# 1 2 3 4 5 6
# 3 4 5 6
# 7 8 9
# 9 7 5 3 2
# Sample Output:
# 1 2 3
# 3 4 5
# 7 8 9
# 9 7 5

def get_zip(z):
    x = zip(*z)
    res = zip(*x)
    return res


lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']

lst = [x.split() for x in lst_in]
res = get_zip(lst)
for _ in range(len(lst_in)):
    print(*next(res))
print('==' * 3)
# another solution

for i in zip(*zip(*lst_in)):
    print(*i, sep='')