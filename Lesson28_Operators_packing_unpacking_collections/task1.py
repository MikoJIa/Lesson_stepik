# Вводится список из семи целых чисел в одну строчку через пробел. Необходимо первые четыре числа занести в переменную
# lst, а остальные три в отдельные переменные x, y, z. Сделать с использованием оператора упаковки. Вывести список lst
# на экран с помощью команды:
# print(*lst)
# Sample Input:
# 56 4 -23 2 0 3 5
# Sample Output:
# 56 4 -23 2


f = list(map(int, input().split()))
*lst, x, y, z = f
print(*lst)

# another solution

*lst, x, y, z = input().split()
print(*lst)