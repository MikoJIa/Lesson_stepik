# Вводятся пункты меню (каждый пункт с новой строки) в формате:
# название_1 URL-адрес_1
# название_2 URL-адрес_2
# ...
# название_N URL-адрес_N
# Необходимо эту информацию представить в виде вложенного кортежа menu в формате:
# ((название_1, URL-адрес_1), (название_2, URL-адрес_2), ... (название_N, URL-адрес_N))
# Результат вывести на экран в виде кортежа командой:
# print(menu)
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# Главная home
# Python learn-python
# Java learn-java
# PHP learn-php
# Sample Output:
# (('Главная', 'home'), ('Python', 'learn-python'), ('Java', 'learn-java'), ('PHP', 'learn-php'))
lst = ['Главная home','Python learn-python','Java learn-java','PHP learn-php']
menu = ()
t = [tuple(i.split()) for i in lst]
menu += tuple(t)
print(menu) # (('Главная', 'home'), ('Python', 'learn-python'), ('Java', 'learn-java'), ('PHP', 'learn-php'))
# enother solution
n = tuple(tuple(i.split()) for i in lst)
print(n)
# enother solution
s = ()

for i in lst:
    s += tuple(i.split()),
print(s)

