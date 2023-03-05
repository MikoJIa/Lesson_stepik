# На вход программы поступает список товаров в формате:
# название_1:цена_1
# ...
# название_N:цена_N
# Необходимо преобразовать этот список в словарь, ключами которого выступают цены (целые числа), а значениями -
# соответствующие названия товаров. Необходимо написать функцию, которая бы принимала на входе словарь и возвращала
# список из наименований трех наиболее дешевых товаров.
# Вызовите эту функцию и отобразите на экране полученный список в порядке возрастания цены в одну строчку через пробел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# смартфон:120000
# яблоко:2
# сумка:560
# брюки:2500
# линейка:10
# бумага:500
# Sample Output:
# яблоко линейка бумага

lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']

def dict_key(x):
    res = {}
    lst = []
    for i in x:
        key, value = i.split(':')
        res[int(value)] = key
        res_dict = sorted(res)[:3]
    for i in res_dict:
        if i in res:
            lst.append(res[i])
    return lst

print(*dict_key(lst_in))


# another solution

def get_cheap(d):
    return list(dict(sorted(d.items())[:3]).values())


dct = {int(b): a for a, b in [x.split(':') for x in lst_in]}
print(*get_cheap(dct))

# another solution

def get_cheap(lst):
    d = dict(map(lambda x: (int(x[1]), x[0]), map(lambda y: y.split(':'), lst)))

    for k, v in sorted(d.items()):
        yield v


x = get_cheap(lst_in)
for _ in range(3):
    print(next(x), end=' ')

# another solution


def fu(d):
    return [x[1] for x in sorted(d.items())[:3]]


gen = (s.split(':') for s in lst_in)
d = {int(b): a for a, b in gen}
print(*fu(d))