# Вводятся три целых положительных числа (максимум трехзначные) через пробел в одну строчку.
# Для двухзначных и однозначных чисел нужно добавить слева незначащие нули так, чтобы все числа содержали по три цифры.
# Вывести на экран полученные числа в столбик.
# Sample Input:
# 8 11 123
# Sample Output:
# 008
# 011
# 123

a, b, c = map(str, input().split())
a = a.rjust(3, '0')
b = b.rjust(3, '0')
c = c.rjust(3, '0')
print(a, b, c, sep='\n')
# the second variant of the solution
[print(i.rjust(3, '0')) for i in input().split()]
# the third solution
print(*map(lambda x: x.rjust(3, '0'), input().split()), sep='\n')
