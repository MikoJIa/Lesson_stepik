# Имеется следующее меню:
# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
# В программе вводится целое число от 1 до 6. Нужно вывести пункт меню, связанный с этим числом. Реализовать программу с использованием операторов if-elif
# Sample Input:
# 2
# Sample Output:
# 2. Строки и списки

m = ['1. Введение в Python',
'2. Строки и списки',
'3. Условные операторы',
'4. Циклы',
'5. Словари, кортежи и множества',
'6. Выход']
n = int(input())
if n == 1:
    print(m[0])
elif n == 2:
    print(m[1])
elif n == 3:
    print(m[2])
elif n == 4:
    print(m[3])
elif n == 5:
    print(m[4])
elif n == 6:
    print(m[5])