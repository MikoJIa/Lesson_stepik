# На вход программы поступают два списка целых чисел (каждый в отдельной строке), записанных в одну строчку через
# пробел. Длины списков могут быть разными. Необходимо первый список отсортировать по возрастанию,
# а второй - по убыванию. Полученные пары из обоих списков сложить друг с другом и получить новый список чисел.
# Результат вывести на экран в виде строки чисел через пробел.
# P. S. Подсказка: не забываем про функцию zip.
# Sample Input:
# 7 6 4 2 6 7 9 10 4
# -4 5 10 4 5 65
# Sample Output:
# 67 14 9 11 10 3

def get_zip(z):
    def two_list_intenger(*args):
        a, b = z(*args)
        res = [i + j for i, j in zip(a, b)]
        return res
    return two_list_intenger


@get_zip
def func(a, b):
    lst = list(map(int, a.split()))
    lst2 = list(map(int, b.split()))
    return sorted(lst), sorted(lst2, reverse=True)

v = input()
x = input()

print(*func(v, x))  # 67 14 9 11 10 3

# another solution

lst_1 = sorted(map(int, input().split()))
lst_2 = sorted(map(int, input().split()))[::-1]

print(*map(sum, zip(lst_1, lst_2)))  # 67 14 9 11 10 3

# another solution

lst1 = sorted(map(int, input().split()))
lst2 = sorted(map(int, input().split()), reverse=True)

print(*map(lambda z, x: z + x, lst1, lst2))  # 67 14 9 11 10 3