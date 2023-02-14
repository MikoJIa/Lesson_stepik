# На вход программы подается вещественное число. Необходимо импортировать модуль math, вызывать функцию ceil
# этого модуля для введенного числа и отобразить результат на экране.
# Sample Input:
# 5.67
# Sample Output:
# 6
from math import ceil as ce

def func_ceil(x):
    return ce(x)


x = float(input())
print(func_ceil(x))

# another solution


print(__import__('math').ceil(float(input())))