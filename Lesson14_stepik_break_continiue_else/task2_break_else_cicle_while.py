# На каждой итерации цикла вводится целое число. Необходимо подсчитать произведение только положительных чисел,
# до тех пор, пока не будет введено значение 0. Реализовать пропуск вычислений с помощью оператора continue,
# а также использовать цикл while. Результат произведения вывести на экран.
# Sample Input:
# 2
# -1
# 3
# 2
# -5
# 7
# 0
# Sample Output:
# 84

sum = 1
d = 1
while d != 0:
    d = int(input('Введите целое число: '))
    if d < 0:
        continue
    if d > 0:
        sum *= d
print(sum)
# another solution
sum = 1
while True:
    n = int(input('Введите целое число: '))
    if n == 0:
        break
    elif n < 0:
        continue
    sum *= n

print(sum)
