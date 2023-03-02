# Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:
# (символ, порядковый индекс)
# Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее. То есть, число пар может
#  быть 10 и менее. Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.
# Программа ничего не должна отображать на экране, только формировать список из кортежей.
# Sample Input:
# Python дай мне силы пройти этот курс до конца!
# Sample Output:
# True


def func(x):
    lst = tuple((item, i,) for i, item in enumerate(x))
    return lst


s = input()
l = list(map(str, s.split()))
res = func(l)
for x in func(l):
    print(x[:11], end=' ')

# another solution

s = input()
l = list(map(str, s.split()))
lst = [(item, i,) for i, item in enumerate(l) if i < 10]
print(lst)

# another solution

lst = list(zip(s, range(len(s))))[:10]
print(lst)