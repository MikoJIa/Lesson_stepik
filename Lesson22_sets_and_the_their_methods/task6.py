# Пользователь с клавиатуры вводит названия городов, пока не введет букву q. Определить общее уникальное число городов,
# которые вводил пользователь. На экран вывести это число. Из коллекций при реализации программы использовать только множества.
# Sample Input:
#Уфа
# Москва
# Тверь
# Екатеринбург
# Томск
# Уфа
# Москва
# q
# Sample Output:
# 5
#
s = []
while True:
    l = input()
    if l == 'q':
        break
    if l not in s:
        s.append(l)
    else:
        s = s
print(len(set(s)))

# enother solution

d = input()
l = set()
while d != 'q':
    l.add(d)
    d = input()
print(len(l))


