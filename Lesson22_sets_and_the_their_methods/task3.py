# Вводится строка, содержащая латинские символы, пробелы и цифры. Необходимо выделить из нее все неповторяющиеся цифры
# (символы от 0 до 9) и вывести на экран в одну строку через пробел их в порядке возрастания значений.
# Если цифры отсутствуют, то вывести слово НЕТ.
# Sample Input:
# Python 3.9.11 - best language!
# Sample Output:
# 1 3 9

s = set(i for i in input())
l = []
fl = 'Нет'
for i in range(0, 10):
    if str(i) in s:
        l.append(i)
if len(l) <= 0:
    print(fl)
else:
    print(*sorted(l))

# enother solution

st = set([u for u in input() if u.isdigit()])
if st:
    print(*sorted(st))
else:
    print('НЕТ')


