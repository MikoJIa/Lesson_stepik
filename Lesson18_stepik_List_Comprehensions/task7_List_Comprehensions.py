# Вводится список вещественных чисел. С помощью list comprehension сформировать список,
# состоящий из элементов введенного списка, имеющих четные индексы (то есть, выбрать все элементы с четными индексами).
# Результат вывести на экран в одну строку через пробел.
# Sample Input:
# 8.5 11.3 1.0 -4.5 11.34 6.45
# Sample Output:
# 8.5 1.0 11.34
lst = [x for x in input().split()]
print(*lst[::2])
# enother solution
lst = [float(item) for i, item in enumerate(input().split()) if i % 2 == 0]
print(*lst)