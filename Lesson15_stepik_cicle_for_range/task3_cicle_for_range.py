# Вводится натуральное число n. С помощью цикла for найти все делители этого числа.
# Найденные делители выводить сразу в столбик без формирования списка.
# Sample Input:
# 12
# Sample Output:
# 1
# 2
# 3
# 4
# 6
# 12

n = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
# enother solution
[print(i) for i in range(1,n+1) if n % i == 0]

