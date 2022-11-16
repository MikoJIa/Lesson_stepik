# Вводится шестизначное число. Определить, является ли оно счастливым.
# (Счастливым называют такое шестизначное число, в котором сумма его первых трех цифр равна сумме его последних трех цифр.)
#  Вывести ДА, если счастливое и НЕТ - в противном случае.
# Sample Input:
# 811235
# Sample Output:
# ДА

num = list(map(int, input()))
a = sum(num[0:3])
b = sum(num[3:7])
if a == b:
    print('ДА')
else:
    print('НЕТ')
