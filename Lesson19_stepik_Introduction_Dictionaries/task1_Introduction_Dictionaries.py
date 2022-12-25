# Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Значениями здесь являются целые числа (см. пример ниже). Необходимо на их основе создать словарь d с помощью функции
# dict() и вывести его на экран командой:
# print(*sorted(d.items()))
# Sample Input:
# one=1 two=2 three=3
# Sample Output:

# ('one', 1) ('three', 3) ('two', 2)
l = input().split()

lst = [l[i].split('=') for i in range(len(l))]
print(lst)
d = dict(lst)
for i in d:
    d[i] = int(d[i])
print(*sorted(d.items()))
# # enother solution
lst = [l[i].split('=') for i in range(len(l))]
d = {}
for i in range(0, len(lst)):
    d[lst[i][0]] = int(lst[i][1])
print(*sorted(d.items()))
# enother solution
lst = [[i.split('=')[0], int(i.split('=')[1])] for i in l]
d = dict(lst)
print(*sorted(d.items()))