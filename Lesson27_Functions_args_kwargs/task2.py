# Объявите функцию с именем get_biggest_city, которой можно передавать произвольное количество названий городов через
# аргументы. Данная функция должна возвращать название города наибольшей длины. Если таких городов несколько, то первый
# найденный (из наибольших). Программу реализовать без использования сортировки.
# Функцию выполнять не нужно, только определить.
# Sample Input:
# Питер Москва Самара Воронеж
# Sample Output:
# Воронеж


def get_biggest_city(*args):
    Max = args[0]
    i = 0
    for x in range(len(args)):
        if len(Max) < len(args[i]):
            Max = args[i]
        i += 1
    return Max


print(get_biggest_city(*list(map(str, input().split()))))

# another solution

def get_biggest_city(*args):
    return max(args, key=len)


print(get_biggest_city(*list(map(str, input().split()))))