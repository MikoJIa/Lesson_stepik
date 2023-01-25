# Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки.
# Будем полагать, что адрес верен, если он обязательно содержит символы '@' и '.',
# а все остальные символы могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит ДА,
# иначе - НЕТ.
# После объявления функции прочитайте (с помощью функции input)
# строку с email-адресом и вызовите функцию с этим аргументом.
# Sample Input:
#
# sc_lib@list.ru
# Sample Output:
#
# ДА

from string import ascii_lowercase as low_lit, digits as dig

def email_addres(email):
    correct = low_lit + dig
    if '@' in email and '_' in email and '.' in email or correct <= email <= correct:
        print('ДА')
    else:
        print('НЕТ')


res = input()
email_addres(res)

def address(email):
    t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
         'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y',
         'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@',
         '.'}
    if 'a' <= email.lower() <= 'z' or '0' <= email <= '9' or 'A' <= email.upper() <= 'Z' or email in '@_.':
        print('ДА')
    else:
        print('НЕТ')


res = input()
address(res)