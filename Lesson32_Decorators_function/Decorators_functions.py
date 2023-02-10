# Декораторы функции
import time


def func_decorator(func):
    def wrapper(*args, **kwargs):  # сделаем эту функцию более универсальной записам в параметры *args, **kwargs
        print("------ что-то делаем перед вызовом функции ------")
        res = func(*args, **kwargs)
        print("------ что-то делаем после вызова функции ------")
        return res
    return wrapper
# сделаем некую переменную функции func_decorator которая будет ссылатся на внутренюю функцию wrapper

def some_func(title, tag):
    print(f"title - {title}, tag - {tag}")
    return f"title - <{tag}>{title}</{tag}>"


some_func = func_decorator(some_func)
res = some_func('Python навсегда!!', tag='h1')
print(res)

# Наш декоратор будет называтся test_time

def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()  # начальное время
        res = func(*args, **kwargs)
        et = time.time()  # конечное время
        dt = et - st  # вычтем разность и узнаем какое время
        print(f"Время работы функции: - {dt} сек.")
        return res
    return wrapper

# Сейчас мы продекорируем функции как это принято


@test_time  # Всё готово, наш декоратор готов теперь наши функции будут показывать поиск времени
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


# get_nod = test_time(get_nod)  # Это декорирование фунции
# get_fast_nod = test_time(get_fast_nod)  # Это декорирование фунции

res = get_nod(2, 1000000)
res1 = get_fast_nod(2, 1000000)
print(res, res1)
