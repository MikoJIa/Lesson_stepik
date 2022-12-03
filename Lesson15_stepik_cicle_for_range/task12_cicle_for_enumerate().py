# Вводится список в виде вещественных чисел в одну строку через пробел.
# С помощью цикла for необходимо найти наименьшее значение в этом списке. Полученный результат вывести на экран.
# Реализовать программу без использования функции min, max и сортировки.
# Sample Input:
# 8.6 9.11 -4.567 -10.0 1.45
# Sample Output:
# -10.0
n = list(map(float, input().split()))
n.sort()
for i in n:
    break
print(n[0], end='')
# # enother solution
a = n[0]
for i in n:
        if i < a:
            a = i
print(a)
# enother solutipn
min = 0
for i, item in enumerate(n):
    if n[min] > item:
        min = i
print(n[min])

