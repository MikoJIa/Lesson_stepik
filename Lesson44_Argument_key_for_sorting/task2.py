# На вход программы поступает строка в формате:
# предмет_1=вес_1
# ...
# предмет_N=вес_N
# Веса предметов заданы целыми числами. Необходимо на основе этих данных сформировать словарь и, затем, на основе этого
# словаря сформировать список предметов по убыванию их веса.
# (В списке должны находиться только наименования предметов без их весов).
# Отобразить полученный результат в виде строки с названиями через пробел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# ножницы=100
# котелок=500
# спички=20
# зажигалка=40
# зеркальце=50
# Sample Output:
# котелок ножницы зеркальце зажигалка спички

lst_in = ['ножницы=100', 'котелок=500', 'спички=20', 'зажигалка=40', 'зеркальце=50']


def dict_sort(x):
    d = {}
    l = []
    for i in x:
        key, val = i.split('=')
        d[int(val)] = key
        res = sorted(d.keys(), reverse=True)
    for i in res:
        if i in d:
            l.append(d[i])
    return l


print(*dict_sort(lst_in))


# another solution

def func(d):
    return [x[1] for x in sorted(d.items(), reverse=True)]


gen = (s.split('=') for s in lst_in)
d = {int(b): a for a, b in gen}
print(*func(d))


# another solution

def get_dict(x):
    d = dict(c.split('=') for c in x)
    return d


res = get_dict(lst_in)
print(*sorted(res, key=lambda x: int(res[x]), reverse=True))