# Вводится четырехзначное целое положительное число. Подумайте, как можно определить итератор для перебора его цифр.
# Выведите цифры этого введенного числа (с помощью итератора) в одну строчку через пробел.
# Sample Input:
# 4387
# Sample Output:
# 4 3 8 7

l = list(input())
i = 0
while i < len(l):
    r = iter(l[i])
    print(next(r),end=' ')
    i += 1