# Вводится строка вещественных чисел через пробел. Необходимо определить, есть ли среди них хотя бы одно отрицательное.
# Вывести True, если это так и False - в противном случае.
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# 8.2 -11.0 20 3.4 -1.2
# Sample Output:
# True


def num_float(num: float) -> bool:
    return num < 0


l = list(map(float, input().split()))
print(any(map(num_float, l)))


# another solution

str_float_num = list(map(float, input().split()))
new_lst = []
for item in str_float_num:
    if item < 0:
        new_lst.append(True)
    else:
        new_lst.append(False)
print(any(new_lst))