# На вход программы поступает список целых чисел, записанных в одну строчку через пробел.
# Необходимо выбрать из них четыре наибольших уникальных значения. Результат вывести на экран в порядке их убывания в
# одну строчку через пробел.
# Sample Input:
# 10 5 4 -3 2 0 5 10 3
# Sample Output:
# 10 5 4 3


def get_sort(s):
    d = []
    res = [i for i in s]
    for i in res:
        if i not in d:
            d.append(i)
        else:
            d = d
    return sorted(d, reverse=True)


a = list(map(int, input().split()))
ls = get_sort(a)
print(*ls[:4])

# another solution


def get_set_sort():
    print(*sorted(set(map(int, input().split())), reverse=True)[:4])


get_set_sort()