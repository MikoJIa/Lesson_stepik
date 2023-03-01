# Вводится список email-адресов в одну строчку через пробел. Среди них нужно оставить только корректно записанные
# адреса. Будем полагать, что к таким относятся те, что используют латинские буквы, цифры и символ подчеркивания.
# А также в адресе должен быть символ "@", а после него символ точки "."
# (между ними, конечно же, могут быть и другие символы).
# Результат отобразить в виде строки email-адресов, записанных через пробел.
# Sample Input:
# abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
# Sample Output:
# abc@it.ru biba123@list.ru sc_lib@list.ru
import string
from string import ascii_letters
import re

def get_mail(x):
    d = []
    chars = string.ascii_letters + string.digits
    for i in x:
        l = (len(i) + 1) // 2
        if chars in i:
            d.append(i)
        if '@' in i[0:l] and '.' in i[l:] and '$' not in i[0:l]:
            d.append(i)
    return d


m = input().split()
print(*get_mail(m))

# another solution

def get_email(x):
    for i in x:
        if i not in string.ascii_letters + string.digits + '@._':
            return False
    indx = x.index('@')
    print(indx)
    if '.' in x[indx:]:
        return True
    return False


name = input().split()
print(*list(filter(get_email, name)))