# Вводятся две строки из слов (слова записаны через пробел). Объявите функцию, которая преобразовывает эти две строки в
# два списка слов и возвращает эти списки.
# Определите декоратор для этой функции, который из двух списков формирует словарь, в котором ключами являются слова из
# первого списка, а значениями - соответствующие элементы из второго списка. Полученный словарь должен возвращаться при
# вызове декоратора.
# Примените декоратор к первой функции и вызовите ее для введенных строк. Результат (словарь d) отобразите на экране
# командой:
# print(*sorted(d.items()))
# Sample Input:
# house river tree car
# дом река дерево машина
# Sample Output:
# ('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')

def dictionary(func):
    def menu(a, b):
        a, b = func(a, b)
        lst = []
        for i in range(len(a)):
            lst.append([a[i], b[i]])
            d = dict(lst)
        return d
    return menu


@dictionary
def func(a, b):
    a = list(map(str, a.split()))
    b = list(map(str, b.split()))
    return a, b



x = input()
c = input()
d = func(x, c)
print(*sorted(d.items()))

# another solution

def dict(func):
    def wrapper(*args, **kwargs):
        return dict(zip(*func(*args, **kwargs)))
    return wrapper


@dict
def menu(s1, s2):
    return s1.split(), s2.split()


s1 = input()
s2 = input()
d = menu(s1, s2)
print(*sorted(d.items))