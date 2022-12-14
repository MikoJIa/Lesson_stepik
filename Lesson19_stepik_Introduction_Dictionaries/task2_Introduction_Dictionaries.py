# На вход программы поступают данные в виде набора строк в формате:
# ключ1=значение1
# ключ2=значение2
# ...
# ключN=значениеN
#
# Ключами здесь выступают целые числа (см. пример ниже).
# Необходимо их преобразовать в словарь d (без использования функции dict()) и вывести его на экран командой:
# print(*sorted(d.items()))
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# 5=отлично
# 4=хорошо
# 3=удовлетворительно
# Sample Output:
# (3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')
l = ['5=отлично','4=хорошо', '3=удовлетворительно']
# lst = [l[i].split('=') for i in range(len(l))]
# d = {}
# for i in range(0, len(lst)):
#     d[int(lst[i][0])] = lst[i][1]
# print(*sorted(d.items()))
# enother solution
d = {}
for i in l:
    key, value = i.split('=')
    print(key, value)
    d[int(key)] = value
print(*sorted(d.items()))
