# Вычисление  факториала натурального числа!!

# n = int(input('Введите натуральное число не более 100 - '))
#
# if n < 1 or n > 100:
#     print('Неверно введено натуральное число')
# else:
#     p = 1
#     for i in range(1, n + 1):
#         p *= i
#     print(f'Факториал числа {n}! равен {p}')

# Нарисуем ёлочку в терминале
for i in range(1, 7):
    print('*' * i)

words = ['Python', 'дай', 'мне', 'силы', 'пройти', 'этот', 'курс', 'до', 'конца']
# s = ''
# for w in words:
#     s += ' ' + w
# print(s) #  Python дай мне силы пройти это курс до конца. перед python есть лишний пробел, сейчас мы его уберём!!
s = ''
fl_first = True
for w in words:
    s += ('' if fl_first else ' ') + w
    fl_first = False
print(s) # Python дай мне силы пройти этот курс до конца. Или просто в принте воспользоватся lstrip() с lstrip() работать
# будет быстрее
# А можно ещё проще
print(' '.join(words)) # Python дай мне силы пройти этот курс до конца и ещё быстрее
# Есть список, в этом списке все двухзначные числа нужно заменить нулями
digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i in range(len(digs)):
    if  10 <= abs(digs[i]) <= 99:
        digs[i] = 0
print(digs) #[4, 3, 100, 0, 0, 1, 0, -8]

# Индекс и значение enumerate(объект)
# программу выше можно перезаписать иначе через enumerate()

for i, d in enumerate(digs):
    if 10 <= abs(d) <= 99:
        digs[i] = 0
print(digs) # [4, 3, 100, 0, 0, 1, 0, -8]
# Преобразование строки из Кириллицы в Латиницу
t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh',
     'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']
start_index = ord('а')
title = 'Программирование на Python - лучший курс'
slug = ''

for i in title.lower():
    if 'а' <= i <= 'я':
        slug += t[ord(i) - start_index]
    elif i == 'ё':
        slug += 'yo'
    elif i in ' !?;:.,':
        slug += '-'
    else:
        slug += i
# цикл while мы используем для того что бы убрать два дефиса подрят
while slug.count('--'):
    slug = slug.replace('--', '-')
print(slug)
