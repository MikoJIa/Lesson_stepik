# Вводятся имена студентов в одну строчку через пробел. На их основе формируется кортеж.
# Отобразите на экране все имена из этого кортежа, которые содержат фрагмент "ва" (без учета регистра).
# Имена выводятся в одну строчку через пробел в нижнем регистре (малыми буквами).
# Sample Input:
# Петя Варвара Венера Василиса Василий Федор
# Sample Output:
# варвара василиса василий

s = tuple(i for i in map(str, input().lower().split()) if 'ва' in i[:])
print(*s)
# enother solution
s = tuple(input().lower().split())
s = list(s)
t = ()
for i in s:
    if 'ва' in i:
        t += (i,)
print(*t)
# enother solution
n = tuple(input().split())

for i in n:
    if 'ва' in i.lower():
        print(i.lower(), end=' ')