# Используя символы малых букв латинского алфавита (строка ascii_lowercase):
# from string import ascii_lowercase
# запишите генератор, который бы возвращал все сочетания из двух букв латинского алфавита. Выведите первые 50 сочетаний
# на экран в строку через пробел.
# Например, первые семь начальных сочетаний имеют вид:
# aa ab ac ad ae af ag
import string
from string import ascii_lowercase


def str1(x):
    res = [f'a{i}' for i in x]
    res2 = [x for x in res[:50]]
    return res2


s = str1(ascii_lowercase)
print(*s)

def func(x):
    gen = (i + j for i in x for j in x)
    for i in range(51):
        print(next(gen), end=' ')
        if i == 50:
            break

func(ascii_lowercase)


# another solution

def func(x):
    gen = (i + j for i in x for j in x)
    s = list(gen)
    print(*s[:50])


func(ascii_lowercase)