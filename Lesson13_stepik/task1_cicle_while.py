# Вводятся два целых положительных числа n и m, причем, n < m. Вывести в строку через пробел квадраты целых чисел в диапазоне [n; m].
# Программу реализовать при помощи цикла while.
# Sample Input:
# 2 4
# Sample Output:
# 4 9 16
n, m = map(int, input().split())
i = n
l = []
while i <= m:
    l.append(i ** 2)
    i += 1
print(*l)
# another solution
start, stop = map(int, input().split())
i = start
while i <= stop:
    print(i ** 2, end=' ')
    i += 1