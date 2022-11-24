# Гражданин 1 января открыл счет в банке, вложив 1000 руб. Каждый год размер вклада увеличивается на 5% от имеющейся суммы.
# Определить сумму вклада через n лет (n - целое положительное число, вводимое с клавиатуры).
# Результат округлить до сотых и вывести на экран. Программу реализовать при помощи цикла while.
# Sample Input:
# 5
# Sample Output:
# 1276.28

n = int(input('Введите количество лет - '))
sum = 1000
year = 0
while n > year:
    sum = sum + (sum / 100 * 5)
    year += 1
print(round(sum, 2))