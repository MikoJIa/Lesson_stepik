# Имеется двумерный кортеж, размером 5 x 5 элементов:
#
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1)
      )
# Вводится натуральное число N (N < 5). Необходимо на основе кортежа t сформировать новый аналогичный кортеж t2 размером
#  N x N элементов. Результат вывести на экран в виде таблицы чисел.
# Sample Input:
# 3
# Sample Output:
# 1 0 0
# 0 1 0
# 0 0 1

n = int(input())
t2 = ()

for i in range(n):
    t2 += t[i][:n],
for x in t2:
    print(*x)
# enother solution
n = int(input())
s = tuple([[t[i][x] for i in range(n)] for x in range(n)])
for x in s:
    print(*x)