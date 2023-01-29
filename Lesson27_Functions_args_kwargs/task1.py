# Объявите функцию с именем get_even, которая принимает произвольное количество чисел в качестве аргументов и возвращает
#  список, составленный только из четных переданных значений.
# Функцию выполнять не нужно, только определить.
# Sample Input:
# 45 4 8 11 12 0
# Sample Output:
# 4 8 12 0


def get_even(*args):
    res = [x for x in args if x % 2 == 0]
    return res


st = get_even(*list(map(int, input().split())))
print(*st)
