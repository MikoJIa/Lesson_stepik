# Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д.
# Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п.,
# а значения - список номеров (следующих в том же порядке, что и во входной строке) с соответствующими кодами.
# Полученный словарь вывести командой:
# print(*sorted(d.items()))
# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])


lst = input().split()
print(lst)
# d = {}
# for i in lst:
#     key = i[0:2]
#     if key not in d.keys():
#         d[key] = [i]
#     else:
#         d[key] += [i]
# print(*sorted(d.items()))
# #enother solution
# n = input().split()
# d = dict([(x[0:2], [i for i in n if x[0:2] == i[0:2]]) for x in n ])
# print(sorted(d.items()))
# enother solution
# lst = input().split()
# d = {}
# for s in lst:
#     c = s[:2]
#     print(c)
#     if c in d:
#         d[c].append(s)
#     else:
#         d[c] = [s]
# print(*sorted(d.items()))