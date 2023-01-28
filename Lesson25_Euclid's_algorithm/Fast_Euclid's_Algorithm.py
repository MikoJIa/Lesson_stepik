import time
# Быстрый Алгоритм Увклида

def fast_Euclid(a, b):
    '''Вычисляется НОД для натуральных чисел a и b
        по быстрому алгоритму Евклида.
        :param a: первое натуральное число
        :param b: второе натуральное число
        :return: НОД
        '''
    if a < b:
        a, b = b, a  # поменяли местами значение, теперь мы знаем где у нас большее значение
    while b != 0:
        a, b = b, a % b
    return a


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
    b = 10000000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('#test 3 - ok')
    else:
        print('#test 3 - fail')


res = fast_Euclid(18, 24)
print(res)
test_nod(fast_Euclid)