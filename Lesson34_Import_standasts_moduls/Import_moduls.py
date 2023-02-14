# в действительности модуль это обычный текстовый файл
from math import ceil as ce, pi
import pprint
from time import gmtime, time # если мы не хотим использовать весь модуль целиком
# откроем все локальные переменные

def ceil(x):
    print('Наша функция')
    return x


pprint.pprint(locals())
a = ce(1.8)
print(a)
print(time())