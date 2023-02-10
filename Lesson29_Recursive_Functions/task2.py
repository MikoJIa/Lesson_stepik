# Вводится список целых чисел в одну строчку через пробел. Необходимо вычислить сумму этих введенных значений, используя
#  рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum. Функция должна возвращать значение суммы.
# (Выводить на экран она ничего не должна).
# Вызовите эту функцию и выведите вычисленное значение суммы на экран.
# Sample Input:
# 8 11 -5 4 3
# Sample Output:
# 21


def get_rec_sum(n):
    length = len(n)
    if length == 1:
        return n[0]
    else:
        return n[0] + get_rec_sum(n[1:])


res = list(map(int, input().split()))
print(get_rec_sum(res))