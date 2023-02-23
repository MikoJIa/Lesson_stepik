# Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной в N
# символов. Например, при N=6, получим адрес: SCrUZo@mail.ru
# Для формирования случайного индекса для строки chars используйте функцию randint модуля random:
# import random
# random.seed(1)
# indx = random.randint(0, len(chars)-1)
# Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно.
# Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).
# Sample Input:
# 8
# Sample Output:
# iKZWeqhF@mail.ru
# WCEPyYng@mail.ru
# FbyBMWXa@mail.ru
# SCrUZoLg@mail.ru
# ubbbPIay@mail.ru


from string import ascii_lowercase, ascii_uppercase
import random
random.seed(1)


def get_passw_mail(N):
    chars = ascii_lowercase + ascii_uppercase
    while True:
        password = ''
        for x in range(N):
            indx = random.randint(0, len(chars)-1)
            password += chars[indx]
        yield password + '@mail.ru'


n = int(input())
gen = get_passw_mail(n)
for i in range(5):
    print(next(gen))