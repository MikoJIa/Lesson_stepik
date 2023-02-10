N = 100  # Глобальная переменная
Width, Height = 1000, 500


def my_func(lst):
    global N  # теперь мы нашу переменную сделали глобальной, и это сразу отразилось на выводе.
    N = 20  # Локальная переменная, эта переменная существует только внутри функции.
    for x in lst:
        n = x + 1 + N
        print(n)


my_func([1, 2, 3])
print(N)

# определим глобальную переменную во вложеной функции
x = 0


def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print('inner', x)  # 2

    inner()
    print('outer', x)  # 2

outer()
print('global', x)  # 0