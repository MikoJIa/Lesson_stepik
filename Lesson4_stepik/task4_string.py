# Написать программу ввода двух слов (через пробел в одну строчку). Определить булевы значения для оператора in проверки вхождения первого слова во второе.
# А также для операторов ==, >, <. Все булевы значения объединить в одну строку через пробел и вывести на экран.
# Sample Input:
# hello python
# Sample Output:
# False False False True

a, b = map(str, input().split())
# c = bool(a in b)
# x = bool(a == b)
# z = bool(a > b)
# v = bool(a < b)
# print(f'{c} {x} {z} {v}')
# Ещё вариант решения
print(a in b, a == b, a < b, a > b, sep=' ')

