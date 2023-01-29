# Имеется словарь, содержащий пункты меню:
# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# Дополнительно вводятся еще пункты меню в виде строк в формате:
# название_1=url_1
# ...
# название_N=url_N
# Необходимо эту введенную информацию преобразовать в словарь и добавить к словарю menu, используя оператор распаковки
# для словарей. На результирующий словарь должна вести переменная menu. Выводить словарь не нужно, только сформировать.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# Города=about-cities
# Машины=read-of-cars
# Самолеты=airplanes
# Sample Output:
# Архив Главная Города Машины Новости Самолеты
# about-cities airplanes archive home news read-of-cars

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']

f = [lst_in[i].split('=') for i in range(len(lst_in))]
d = dict(f)
m = ({**d, **menu})
print(*sorted({*m}))
print(*sorted({*m.values()}))

# another solution

d = dict()
for i in lst_in:
    key, value = i.split('=')
    d[key] = value
menu = {**menu, **d}
print(*menu)
print(*menu.values())