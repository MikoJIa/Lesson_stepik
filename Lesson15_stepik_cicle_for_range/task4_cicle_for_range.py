# Вводится натуральное число n. С помощью цикла for определить, является ли оно простым
# (то есть, делится нацело только на само себя и на 1). Вывести на экран ДА, если n простое и НЕТ - в противном случае.
# Sample Input:
# 11
# Sample Output:
# ДА

n = int(input())

for i in range(2,int(n/2)+1):
    if n % i == 0 and n > 1:
        print('НЕТ')
        break
else:
    print('ДА')
# enother solution
n = int(input())
flag = 'ДА'

for i in range(2, n // 2):
    if n % i == 0:
        flag = 'НЕТ'
else:
    print(flag)