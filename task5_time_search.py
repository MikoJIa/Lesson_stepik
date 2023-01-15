# На вход вашему серверу пришло время в минутах, которое провел человек на сайте , а также время начала сессии.
# Вам нужно определить сколько времени было на цифровых часах у человека, когда он закрывал сайт.
# Ввод:
# time_mins – количество минут, которое провел на сайте
# start_hours – время в часах, когда человек зашел на сайт
# start_mins – время в минутах, когда человек зашел на сайт
# Вывод:
# через пробел
# h – час закрытия сайта
# m – минута закрытия сайта
# Sample Input 1:
# 120
# 19
# 0
# Sample Output 1:
# 21 0
# Sample Input 2:
# 125
# 23
# 5
# Sample Output 2:
# 1 10

time_min = int(input('Введите число '))
start_hours = int(input('Введите число '))
start_min = int(input('Введите число '))

close_h = time_min // 60 + start_hours
close_min = start_min +time_min % 60

if close_h > 24:
    close_h = close_h - 24
if close_min >= 60:
    close_min = close_min - 60
    close_h += 1
print(f'{close_h} {close_min}')

# enother solution

time_mins = int(input())
start_hours = int(input())
start_mins = int(input())

result_time = time_mins + start_hours * 60 + start_mins
print(result_time // 60 % 24, result_time % 60)