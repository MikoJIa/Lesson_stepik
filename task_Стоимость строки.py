import math
from decimal import Decimal, ROUND_HALF_DOWN
# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ
# (в том числе пробел) стоит 6060 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести стоимость строки.


def price_str(x):
    res = len(x *60)
    rub = math.floor(res/100)
    cop = res%100
    return f'{rub} р. {cop} коп.'


print(price_str(input()))

# another solution

string = input()
price = 60 * len(string)

print(f'{price // 100} р. {price % 100} коп.')


