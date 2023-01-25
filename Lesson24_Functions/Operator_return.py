def get_sqrt(x):
    res = None if x < 0 else x ** 0.5 # тут у нас res будет возвращать None если икс меньше нуля, в ином случае икс
    # будем возвадить на 0.5
    # а что если мы хотим передать две переменные, можно передать через картеж
    return (res, x)

a, b = get_sqrt(49)
print(a, b)  #  0.7 корень квадратный из 49


def get_max2(x, y):
    return x if x > y else y  # записываем через тернарный оператор

z, v, c = 5, 7, 10
print(get_max2(z, get_max2(v, c))) # 10


# теперь сделаем функцию в функции
# Такой подход в программирование называется функциональный подход
def get_max2(x, y):
    return x if x > y else y


def get_max3(x,y, n):
    return get_max2(x, get_max2(y, n))


PERIMETR = True
if PERIMETR:
    def get_rect(a, b):
        return 2 * (a + b)  # периметр прямоугольника
else:
    def get_rect(a, b):
        return  a + b  # площадь прямоугольника



z, v, c = 5, 7, 10
print(get_max3(z, v, c))  # 10
print(get_rect(1.5, 3.8))  # 10.6 мы получили периметр прямоугольника, по тому что у нас PERIMETR = True, если бы мы
# в место True обозначили False, то тогда у нас посчитало бы площадь прямоугольника

# А теперь попробуем использовать функцию в цикле

def even(x):
    return x % 2 == 0


for i in range(1, 20):
    if even(i):
        print(i, end=' ')  # 2 4 6 8 10 12 14 16 18