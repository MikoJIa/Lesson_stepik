# Вводится строка. Нужно создать итератор для перебора символов этой строки.
# Затем, перебрать через созданный итератор все символы до первого пробела.
# В процессе перебора символы выводить на экран в одну строчку друг за другом (без пробелов).
# Гарантируется, что во введенной строке имеется хотя бы один пробел.
# Sample Input:
# Возможно-это будет полезно
# Sample Output:
# Возможно-это

l = iter(input())
while True:
    i = next(l)
    if i == ' ':
        break
    print(i, end='')
# # enother solution
l = list(input().split())
r = iter(l)
print(next(r))
# enother solution
st, i = input(), 0
st1 = iter(st)
while st[i] != ' ':
    print(next(st1),end='')
    i += 1
