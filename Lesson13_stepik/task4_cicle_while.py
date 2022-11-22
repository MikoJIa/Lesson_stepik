# На каждой итерации цикла пользователь вводит целое число. Цикл продолжается, пока не встретится число 0.
# Необходимо вычислить сумму введенных в цикле чисел и вывести результат на экран. Программу реализовать при помощи цикла while.
# Sample Input:
# 8
# 11
# 2
# -4
# 0
# Sample Output:
# 17

# сделал через try except пото-му что, возникала ошибка: ValueError: invalid literal for int() with base 10: ''
sum = 0
while True:
    try:
        a = int(input())
    except ValueError:
        sum += a
    if a == 0:
        break
print(sum)



