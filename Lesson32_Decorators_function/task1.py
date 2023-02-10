# Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам: width и height - ширина
#  и высота прямоугольника. И возвращает результат (сама ничего на экран не выводит). То есть, функция имеет сигнатуру:
# def get_sq(width, height): ...
# Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):
# "Площадь прямоугольника: <значение>"
# Вызывать функцию и декоратор не нужно, только объявить. Применять декоратор к функции также не нужно.
# Sample Input:
# 8 11
# Sample Output:
# Площадь прямоугольника: 88

def func_show(x):
    def func(*args, **kwargs):
        s = x(*args, **kwargs)
        print(f'Площадь прямоугольника: {s}')
        return s
    return func

@func_show
def get_sq(width, height):
    return width * height


a, b = map(int, input().split())
s = get_sq(a, b)

# another solution


def show(x):
    def func1(*args, **kwargs):
        print(f'Площадь прямоугольника: {x(*args, **kwargs)}')
    return func1

@show
def sqrt(width, heigth):
    return width * heigth


a, b = map(int, input().split())
res = sqrt(a, b)

