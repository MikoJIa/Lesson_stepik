# Вводится натуральное число n. Вывести первое найденное натуральное число (то есть, перебирать числа, начиная с 1),
# квадрат которого больше значения n. Реализовать программу с использованием цикла while.
# Sample Input:
# 10
# Sample Output:
# 4

n = int(input())
i = 1
while n:
    if i**2 > n:
        print(i, end='')
        break
    i += 1

