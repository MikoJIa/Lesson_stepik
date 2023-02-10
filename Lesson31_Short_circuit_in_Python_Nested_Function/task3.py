# Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s
# (s - строка, параметр внутренней функции). Далее, на вход программы поступает строка и ее нужно поместить в тег h1 с
# помощью реализованного замыкания. Результат выведите на экран.
# P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
# Sample Input:
# Balakirev
# Sample Output:
# <h1>Balakirev</h1>


def outer_func(msg):
    def inner_func(s='h1'):
        return f'<{s}>{msg}</{s}>'
    return inner_func


name = input()
f = outer_func(name)
print(f())