#  На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# True


s = input()
s_lst = s.split()
g = (j.split('=') for j in s_lst)
tp = tuple(tuple(map(str, x)) for x in g)
print(tp)

# another solution

tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))
print(tp)
