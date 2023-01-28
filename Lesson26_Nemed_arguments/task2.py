# Объявите функцию с именем check_password, которая принимает аргумент - строку (пароль) и имеет один формальный
# параметр chars с начальным значением в виде строки "$%!?@#". Функция должна проверять: есть ли в пароле хотя бы один
# символ из chars и что длина пароля не менее 8 символов. Если проверка проходит, то функция возвращает True,
#  иначе - False.
# P. S. Вызывать функцию не нужно, только объявить.
# Sample Input:
# 12345678!
# Sample Output:
# True
from re import search

def check_password(a, chars="$%!?@#"):
    for i in range(len(chars)):
        if chars[i] in a and len(a) >= 8:
            return True
    else:
        return False


res = ','.join(str(input()))
print(check_password(res))