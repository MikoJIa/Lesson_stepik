# Вводится натуральное число N. Необходимо определить функцию-генератор с именем get_sum, которая бы возвращала текущую
# сумму чисел последовательности длины N в диапазоне целых чисел [1; N]. Например:
# - для первого числа 1 сумма равна 1;
# - для второго числа 2 сумма равна 1+2 = 3
# ....
# - для N-го числа сумма равна 1+2+...+(N-1)+N
# Реализовать функцию-генератор get_sum без использования коллекций. Вызывать ее не нужно, только определить.
# Sample Input:
# 5
# Sample Output:
# 1 3 6 10 15

def get_sum(N):
    sum_num = 1
    for x in range(1, N):
        if sum_num == 1:
            print(1, end=' ')
        sum_num += x
        yield sum_num + x


n = int(input())
get_sum(n)
for i in get_sum(n):
    print(i, end=' ')

# another solution


def get_sum2(N):
    summ = 0
    for i in range(1, N+1):
        summ += i
        yield summ


s = int(input())
get_sum2(s)
for i in get_sum2(s):
    print(i, end=' ')