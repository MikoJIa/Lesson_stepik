# Вводится целое положительное число n. Вычислить и вывести на экран сумму: 1 + 1/2 + 1/3 + ... + 1/n
# с точностью до тысячных (три знака после запятой). Программу реализовать при помощи цикла while.
# Sample Input:
# 8
# Sample Output:
# 2.718


n = int(input())
i = 2
sum = 1
while i <= n:
    sum = sum + (1 / i)
    i += 1
print(round(sum, 3))