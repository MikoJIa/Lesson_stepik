# Вводятся целые числа в одну строку через пробел. На их основе формируется кортеж.
# Необходимо создать еще один кортеж с уникальными (не повторяющимися) значениями из первого кортежа.
# Результат отобразите в виде списка чисел через пробел.
# P. S. Подобные задачи решаются, как правило, с помощью множеств, но в качестве практики пока обойдемся без них.
# Sample Input:
# 8 11 -5 -2 8 11 -5
# Sample Output:
# 8 11 -5 -2

s = tuple(map(int, input().split()))
t = ()
for i in s:
    if i not in t:
        t += (i,)
print(*t)
# enother solution
n = tuple(map(int, input().split()))
d = tuple(dict.fromkeys(n))
print(*d)
# enother solution
print(*tuple(dict.fromkeys(map(int,input().split()))))