# Вводится натуральное число, которое может быть определено простыми множителями 1, 2, 3, 5 и 7.
# Необходимо разложить введенное число на указанные простые множители и проверить, содержит ли оно множители 2, 3 и 5
# (все указанные множители)? Если это так, то вывести ДА, иначе - НЕТ.
# Sample Input:
# 210
# Sample Output:
# ДА

a = int(input())
s = set()
b = {2, 3, 5}
for i in range(1, a + 1):
    if a%i == 0:
        s.add(i)
        s.intersection_update(b)
if b == s:
    print('ДА')
else:
    print('НЕТ')

# enother solution

N = int(input())
print(("НЕТ", "ДА")[{i for i in range(1, 8) if N%i == 0} >= {2, 3, 5}])

