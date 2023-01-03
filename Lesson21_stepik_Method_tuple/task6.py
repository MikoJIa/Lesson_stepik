# Вводятся целые числа в одну строку через пробел. На их основе формируется кортеж.
# Необходимо найти и вывести все индексы неуникальных (повторяющихся) значений в этом кортеже.
# Результат отобразите в виде строки чисел, записанных через пробел.
# Sample Input:
# 5 4 -3 2 4 5 10 11
# Sample Output:
# 0 1 4 5

s = tuple(map(int, input().split()))
t = ()
s = list(s)
for i in range(len(s)):
    if s.count(s[i]) > 1:
        t += (i,)
print(*t)
# enother solution
n = tuple(map(int,input().split()))
t = tuple(i for i, x in enumerate(n) if n.count(x) > 1)
print(*t)
