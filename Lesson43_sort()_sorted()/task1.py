# На вход поступает список целых чисел, записанных в одну строчку через пробел. Преобразуйте сначала эту строку в список
# из целых чисел, а затем список в кортеж из целых чисел. То есть, в программе будет две разные коллекции: список и
# кортеж. Отсортируйте по возрастанию значений эти коллекции методом sort, если это возможно,
# а иначе - примените функцию sorted.
# На экран ничего выводить не нужно, только сформировать две отсортированные коллекции:
# lst (список) - результат сортировки списка; tp_lst (кортеж) - результат сортировки кортежа.
# P. S. На результаты сортировок обязательно должны ссылаться переменные с именами lst и tp_lst!
# Sample Input:
# -2 -1 8 11 4 5
# Sample Output:
# True


# def lst(a):
#     lst = [int(i) for i in a.split()]
#
#     return sorted(lst)
#
#
# def tp_lst(b):
#     tp_lst = map(int, b.split())
#     return tuple(sorted(tp_lst))
#
#
# s = input()
# print(lst(s), tp_lst(s), sep='\n')

# another solution

# s = input()
# lst = [int(i) for i in s.split()]
# lst.sort()
# tp_lst = tuple(i for i in lst)
# print(lst, tp_lst, sep='\n')

# another solution

s = input()

def get_sort(x):
    try:
        x.sort()
        return x
    except AttributeError:
        return type(x)(sorted(x))

lst = list(map(int, s.split()))
tp_lst = tuple(map(int, s.split()))

print(get_sort(lst))
print(get_sort(tp_lst))