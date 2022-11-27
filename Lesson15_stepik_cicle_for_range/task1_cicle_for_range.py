# Вводятся целые числа в одну строчку через пробел. Необходимо преобразовать эти данные в список целых чисел.
# Затем, перебрать этот список в цикле for и просуммировать все нечетные значения. Результат вывести на экран.
# Sample Input:
# 8 11 -2 4 0 13 19 12 7
# Sample Output:
# 50

l = map(int,input().split())
lst = list(l)
s = 0
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        s += lst[i]
print(s)

# enother solution
for i in lst:
    if i % 2 == 1:
        s += i
print(s)

# enother solution list comprehension
lst = sum([x for x in map(int, input().split()) if x % 2 == 1])
print(lst)
