# Вводится натуральное число n. Необходимо сформировать список с помощью list comprehension,
# состоящий из делителей числа n (включая и само число n). Результат вывести на экран в одну строку через пробел.
# Sample Input:
# 10
# Sample Output:
# 1 2 5 10

n = int(input())
lst = [int(x) for x in range(1, n+1) if n % x == 0]
print(*lst)