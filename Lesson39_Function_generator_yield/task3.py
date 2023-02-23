# Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор, которая бы выдавала пароль длиной N
# символов из случайных букв, цифр и некоторых других знаков. Для получения последовательности допустимых символов для
# генерации паролей в программе импортированы две строки: ascii_lowercase, ascii_uppercase (см. листинг ниже),
# на основе которых формируется общий список:
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N и
# делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. Сгенерировать случайный индекс indx в
# диапазоне [a; b] для символа можно с помощью функции randint модуля random:
# import random
# random.seed(1)
# indx = random.randint(a, b)
# Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки).
# Sample Input:
# 10
# Sample Output:
# riGp?58WAm
# !dX3a5IDnO
# dcdbWB2d*C
# 4?DSDC6Lc1
# mxLpQ@2@yM
from string import ascii_lowercase, ascii_uppercase
import random
random.seed(1)


def get_password(N):
        chars = ascii_lowercase + ascii_uppercase + '0123456789!?@#$*'
        str = ''
        while True:
            for i in range(N):
                if len(str) != N:
                    str += chars[random.randint(0, len(chars))]
            yield str



s = int(input())
print(next(get_password(s)))
print(next(get_password(s)))
print(next(get_password(s)))
print(next(get_password(s)))
print(next(get_password(s)))

# another solution

def get_password(c):
    def wrappes(b):
        res = c(b)
        count = 0
        for i in res:
            count += 1
            if count == 6:
                break
            else:
                print(i)

    return wrappes
@get_password
def func(N):
    chars = ascii_lowercase + ascii_uppercase + '0123456789!?@#$*'
    sr = ''
    while True:
        for i in range(N):
            if len(sr) != N:
                sr += chars[random.randint(0, len(chars))]
        yield sr
        sr = ''


s = int(input())
func(s)

# another solution

def psw(N):
    chars = ascii_lowercase + ascii_uppercase + '0123456789!?@#$*'
    strg = ''
    for j in range(5):
        for i in range(N):
            strg += chars[random.randint(0, len(chars))]
        yield strg
        strg = ''


s = int(input())
psw(s)
for i in psw(s):
    print(i)

# another solution

def get_pas(N):
    while True:
        chars = ascii_lowercase + ascii_uppercase + '0123456789!?@#$*'
        passw = ''
        for i in range(N):
            indx = random.randint(0, len(chars) - 1)
            passw += chars[indx]
        yield passw


n = int(input())
gen = get_pas(n)
for i in range(5):
    print(next(gen))