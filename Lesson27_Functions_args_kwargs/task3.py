# Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника. На вход этой функции
# передаются N длин сторон через аргументы. Дополнительно могут быть указаны именованные аргументы:
# type - булево значение True/False
# color - целое числовое значение
# closed - булево значение True/False
# width - целое значение
#
# Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров в порядке
# их перечисления в тексте задания (если они были переданы). Если какой-либо параметр отсутствует, его возвращать
# не нужно (пропустить).
# Функцию выполнять не нужно, только определить.


def get_data_fig(*args, **kwargs):
    l = []
    P = 0
    for x in args:
        P += x
    l.append(P)
    if 'type' in kwargs:
        l.append(kwargs['type'])
    if 'color' in kwargs:
        l.append(kwargs['color'])
    if 'closed' in kwargs:
        l.append(kwargs['closed'])
    if 'width' in kwargs:
        l.append(kwargs['width'])
    l = tuple(l)
    return (l)


print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))

# another solution

def get_data(*args, **kwargs):
    res = sum(args)
    kwargs = (tuple(kwargs[i] for i in kwargs if i in kwargs.keys()))
    return (res, *kwargs)


print(get_data(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))