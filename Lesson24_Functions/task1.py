# Объявите функцию, которая принимает список, находит максимальное, минимальное и сумму значений этого списка и выводит
# результат в виде строки (без кавычек):
# "Min = v_min, max = v_max, sum = v_sum"
#
# где v_min, v_max, v_sum - вычисленные значения минимального, максимального и суммы значений списка.
#
# После объявления функции прочитайте (с помощью функции input) список целых чисел,
# записанных в одну строку через пробел, и вызовите функцию с этим списком.
# Sample Input:
# 8 11 5 -10 12 0
# Sample Output:
# Min = -10, max = 12, sum = 26

def min_numbers(lst: int):
    v_min = lst[0]
    for i in lst:
        if v_min > i:
            v_min = i
    print(f'Min = {v_min}', end=' ')

    v_max = lst[0]
    for x in lst:
        if v_max < x:
            v_max = x
    print(f'max = {v_max}', end=' ')

    summ = 0
    for z in lst:
        summ += z
    print(f'sum = {summ}')


min_numbers(list(map(int, input().split())))

# another solution

def min_nam_sum(number):
    text = f'Min = {min(number)}, max = {max(number)}, sum = {sum(number)}'
    print(text)

res = list(map(int, input().split()))
min_nam_sum(res)


