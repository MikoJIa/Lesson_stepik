# Вводятся данные в формате:
# <день рождения 1> имя_1
# <день рождения 2> имя_2
# ...
# <день рождения N> имя_N
# Дни рождений и имена могут повторяться. На их основе сформировать словарь и вывести его в формате (см. пример ниже):
# день рождения 1: имя1, ..., имяN1
# день рождения 2: имя1, ..., имяN2
# ...
# день рождения M: имя1, ..., имяNM
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# 3 Сергей
# 5 Николай
# 4 Елена
# 7 Владимир
# 5 Юлия
# 4 Светлана
# Sample Output:
# 3: Сергей
# 5: Николай, Юлия
# 4: Елена, Светлана
# 7: Владимир

lst = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
d = {}
lst_in = [x.split() for x in lst]

for i in lst_in:
    key, value = i
    if key not in d:
        d[key] = [value]
    else:
        d[key] += [value]

for key, value in d.items():
    print(key + ':', ', '.join(value))
# enother solution
for i in lst_in:
    key, value = i.split()
    d[key] = d.get(key, []) + [value]

for key, value in d.items():
    print(f'{key}: ', end='')
    print(*value, sep=', ')
# enother solution
for pair in lst_in:
    key = pair[0]
    value = pair[1]
    if key not in d:
       d[key] = [value]
    else:
        d[key].append(value)
for k, v in d.items():\
    print(k + ':', ', '.join(v))