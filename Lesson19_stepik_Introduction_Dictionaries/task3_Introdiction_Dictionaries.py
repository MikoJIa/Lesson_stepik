# Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Необходимо на их основе создать словарь, затем проверить, существуют ли в нем ключи со значениями: 'house', 'True' и '5'
# (все ключи - строки). Если все они существуют, то вывести на экран ДА, иначе - НЕТ.
# Sample Input:
# вологда=город house=дом True=1 5=отлично 9=божественно
# Sample Output:
# ДА

lst = input().split()
d = {}
for i in lst:
    key, value = i.split('=')
    d[key] = value
if 'house' not in d or 'True' not in d or '5' not in d:
    print('НЕТ')
else:
    print('ДА')
# enother solution
d = dict([i.split('=') for i in input().split()])
print(d)
print('ДА' if 'house' in d or 'True' in d or '5' in d else 'НЕТ')