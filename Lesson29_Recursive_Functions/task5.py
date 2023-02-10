# Имеется следующий многомерный список:
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d.
# Функция должна возвращать новый созданный одномерный список.  (Только возвращать, выводить на экран ничего не нужно.)
# Вызывать функцию не нужно, только объявить со следующей сигнатурой:
# def get_line_list(d,a=[]): ...
# где d - исходный список; a - новый формируемый.

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

def get_line_list(d, a=[]):
    for i in d:
        if type(i) != list:
            a.append(i)
        elif type(i) == list:
            get_line_list(i)
    return a


get_line_list(d, a=[])
