# (На использование цикла while). Начав тренировки, лыжник в первый день пробежал 10 км. Каждый следующий день он
# увеличивал пробег на 10 % от пробега предыдущего дня. Определить в какой день он пробежит больше x км
# (натуральное число x вводится с клавиатуры). Результат (искомый день) вывести на экран.
# Sample Input:
# 20
# Sample Output:
# 9

x = int(input())
day_first = 10
day = 1
while x > day_first:
    if day_first > x:
        break
    day_first += day_first * 0.1
    day += 1
print(day)
