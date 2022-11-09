
# string.format(*args)
name = 'Cергей'
age = 18
print('Меня зовут {0}, мне {1} лет и я люблю Python!!!'.format(name, age))
# Можно прямо в format() переназначить переменные для удобства!!
print('Меня зовут {fio}, мне {old} лет и я люблю Python!!!'.format(fio = name, old = age))
# f-string
print(f'Меня зовут {name}, мне {age} лет и я люблю Python!!!')
print(f'Меня зовут {name.upper()}, мне {age * 2} лет и я люблю Python!!!')

# a, b = map(int, input().split())
# c = abs(a)
# d = abs(b)
# num_max = max(c, d)
# num_min = min(c, d)
# print(f'{num_min} {num_max}')
# print(f'{min(a,b)} {max(a,b)}')

