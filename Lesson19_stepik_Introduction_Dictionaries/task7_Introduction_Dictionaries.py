# Пользователь вводит в цикле целые положительные числа, пока не введет число 0.
# Для каждого числа вычисляется квадратный корень (с точностью до сотых) и значение выводится на экран (в столбик).
# С помощью словаря выполните кэширование данных так, чтобы при повторном вводе того же самого числа результат не
# вычислялся, а бралось ранее вычисленное значение из словаря. При этом на экране должно выводиться:
# значение из кэша: <число>
# Sample Input:
# 1
# 2
# 3
# 3
# 2
# 4
# 0
# Sample Output:
# 1.0
# 1.41
# 1.73
# значение из кэша: 1.73
# значение из кэша: 1.41
# 2.0
import sys
import math
d = {}
while True:
    number = int(input())
    if number == 0:
        sys.exit()
    if number not in d:
        d[number] = round(math.sqrt(number), 2)
        print(d[number])
    else:
        print(f'Значение из кэша {d[number]}')
    pass
# enother solution
n = int(input())
D = {}

while n != 0:
    if n in D:
        print(f'значение из кэша: {D[n]}')
    else:
        D[n] = round(math.sqrt(n), 2)
        print(D[n])
    n = int(input())
# enother solution
d = {}

while True:
    key = int(input())
    if key == 0:
        break
    elif key not in d:
        d[key] = round(math.sqrt(key), 2)
        print(d[key])
    else:
        print(f'значение из кэша: {d[key]}')