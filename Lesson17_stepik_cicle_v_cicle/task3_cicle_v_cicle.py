# Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n, то есть, в диапазоне
# [2; n). Результат вывести на экран в строчку через пробел.
# Sample Input:
# 11
# Sample Output:
# 2 3 5 7

n = int(input())
l = []
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        l.append(i)
print(*l, end='')