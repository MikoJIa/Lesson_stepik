# Нахождение общего наибольшего делителя с помощью алгоритма Евклида
import time


def Euclid(a, b):
    '''Вычисляется НОД для натуральных чисел a и b
    по алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    '''

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

# Теперь давайте протестируем нашу функцию, создадим другую функцию тест
def test_nod(func):
    # --- тест № 1 -------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('#test 1 - ok')
    else:
        print('#test 1 - fail')

    # --- тест № 2 -------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('#test 2 - ok')
    else:
        print('#test 2 - fail')

    # --- тест № 3 -------------
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('#test 3 - ok')
    else:
        print('#test 3 - fail')
# x, c = 18, 24
# help(Euclid)
# print(Euclid(x, c))
test_nod(Euclid)

