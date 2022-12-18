# Вводятся два списка целых чисел одинаковой длины каждый с новой строки.
# С помощью list comprehension сформировать третий список, состоящий из суммы соответствующих пар чисел введенных списков.
# Результат вывести на экран в одну строку через пробел.
# Sample Input:
# 1 2 3 4 5
# 6 7 8 9 10
# Sample Output:
# 7 9 11 13 15

n = list(map(int, input().split()))
print(n)
m = list(map(int, input().split()))
print(m)
lst = [i + j for i, j in zip(n,m)]
print(*lst)
# enother solution
a = input().split()
b = input().split()
lst = [int(a[i]) + int(b[i]) for i in range(len(a))]
print(*lst)