# Вводятся два списка целых чисел. Необходимо попарно перебрать их элементы и перемножить между собой.
# При реализации программы используйте функции zip и map. Выведите на экран первые три значения, используя функцию next.
#  Значения выводятся в строчку через пробел. (Полагается, что три выходных значения всегда будут присутствовать).
# Sample Input:
# -7 8 11 -1 3
# 1 2 3 4 5 6 7 8 9 10
# Sample Output:
# -7 16 33

a = map(int, input().split())
b = map(int, input().split())
res = [i * j for i, j in zip(a, b)]
print(*res[:3])

# another solution

m = map(lambda x: x[0] * x[1], zip(map(int, input().split())), zip(map(int, input().split())))
print(next(m), next(m), next(m))

# another solution

def mult(x):
    return x[0] * x[1]


lst1 = map(int, input().split())
lst2 = map(int, input().split())
res = map(mult, zip(lst1, lst2))
for _ in range(3):
    print(next(res), end=' ')
