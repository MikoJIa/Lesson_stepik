# Вводится строка целых чисел через пробел. Необходимо определить, являются ли все эти числа четными. Вывести True,
# если это так и False - в противном случае.
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# 2 4 6 8 22 56
# Sample Output:
# True


def an_even_number(x: int) -> bool:
    return x % 2 == 0


l = list(map(int, input().split()))
res = all(map(an_even_number, l))
print(res)