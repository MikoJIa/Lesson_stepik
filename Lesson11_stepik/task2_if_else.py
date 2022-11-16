# Вводится четырехзначное число. Проверить, что оно оканчивается на цифру 7. Вывести на экран ДА, если это так и
# НЕТ - в противном случае.
# Sample Input:
# 8117
# Sample Output:
# ДА

a = int(input())
if a % 10 == 7:
    print('ДА')
else:
    print('НЕТ')
# another  solution
print('ДА' if input()[-1] == '7' else 'НЕТ')