# Вводится таблица целых чисел. Используя функцию map и генератор списков, преобразуйте список строк lst_in
# (см. листинг) в двумерный список с именем lst2D, содержащий целые числа.
# Выводить на экран ничего не нужно, только сформировать список lst2D на основе введенных данных.
# Sample Input:
# 8 11 -5
# 3 4 10
# -1 -2 3
# 4 5 6
# Sample Output:
# True

lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '-4 5 6']
lst = [x.split() for x in lst_in]
lst1D = [int(lst[x][j]) for x in range(0, len(lst)) for j in range(0, len(lst)-1)]
n = int(len(lst1D) ** 0.5)
lst2D = [[abs(lst1D[j]) for j in range(i, i + n, 1)] for i in range(0, len(lst1D), n)]
print(lst2D)

# another solution

lst2D = list(list(map(int, x.split()))for x in lst_in)
print(lst2D)
