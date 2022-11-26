# Вводится список имен студентов в одну строчку через пробел. Определить, что хотя бы одно имя в этом списке начинается
# и заканчивается на ту же самую букву (без учета регистра). Реализовать программу с использованием цикла while и
# оператора break. Вывести ДА, если условие выполняется и НЕТ - в противном случае.
# Sample Input:
# Петр Анна Иван Сергей Михаил Федор
# Sample Output:
# ДА


lst = list(input().lower().split())

i = 0
while i < len(lst):
    if lst[i][:1] == lst[i][-1:]:
        print('ДА')
        break
    i += 1
else:
    print('НЕТ')
# another solution
lst = list(input().split())
res, i = 'НЕТ', len(lst)
while i:
    i -= 1
    if lst[i][:1].lower() == lst[i][-1:].lower():
        res = 'ДА'
        break
print(res)
