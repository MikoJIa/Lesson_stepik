# Вводится стоимость одной книги x рублей (вещественное число).
# Необходимо вывести на экран в строчку через пробел стоимости 2, 3, ... 10 таких книг с точностью до десятых.
# Программу реализовать при помощи цикла while.
# Sample Input:
# 34.6
# Sample Output:
# 69.2 103.8 138.4 173.0 207.6 242.2 276.8 311.4 346.0

x = float(input())
i = 1
while i <= 10:
    print(round(x * i, 1), end=' ')
    i += 1
# another solution
a = float(input())
i = 2
while i < 11:
    print(f'{i*a:.1f}',end=' ')
    i += 1