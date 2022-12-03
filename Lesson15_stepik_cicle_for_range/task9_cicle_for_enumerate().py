#  В виде строки записано арифметическое выражение, например:
# "10 + 25 - 12"
# или
# "10 + 25 - 12 + 20 - 1 + 3"
# и т. д. То есть, количество действий может быть разным.
# Необходимо выполнить вычисление и результат отобразить на экране.
# Полагается, что в качестве арифметических операций здесь используется только сложение (+) и вычитание (-),
# а в качестве операндов - целые неотрицательные числа. Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.
# Sample Input:
# 10+25 - 12
# Sample Output:
# 23

s = input()
s = s.replace(' ','')
s = s.replace('+','_+')
s = s.replace('-','_-')
k = list(map(int, s.split('_')))
print(sum(k))
# enother solution
s = input().strip().replace(' ', '')
print(s) # 10+25-12
res = 0
lst = s.replace('-', '+-').split('+')
print(lst)
for n in lst:
    res += int(n)
print(res)
# enother solution
s = input().replace('+', ' + ').replace('-', ' - ').split()
summ = int(s[0])
for i, item in enumerate(s):
    if item == '+':
        summ += int(s[i + 1])
    elif item == '-':
        summ -= int(s[i + 1])
print(summ)
