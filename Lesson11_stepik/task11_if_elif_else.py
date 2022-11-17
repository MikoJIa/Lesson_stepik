# Вводится порядковый номер дня недели (1, 2, ..., 7). Вывести на экран его название
# (понедельник, вторник, среда, четверг, пятница, суббота, воскресенье). Программу реализовать с использованием операторов if-elif.
# Sample Input:
# 2
# Sample Output:
# вторник

days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
d = int(input())
if d == 1:
    print(days[0])
elif d == 2:
    print(days[1])
elif d == 3:
    print(days[2])
elif d == 4:
    print(days[3])
elif d == 5:
    print(days[4])
elif d == 6:
    print(days[5])
elif d == 7:
    print(days[6])
# another solution
days = {1:'понедельник', 2:'вторник', 3:'среда', 4:'четверг', 5:'пятница', 6:'суббота', 7:'воскресенье'}
d = int(input())
if d == 1:
    print(days[1])
elif d == 2:
    print(days[2])
elif d == 3:
    print(days[3])
elif d == 4:
    print(days[4])
elif d == 5:
    print(days[5])
elif d == 6:
    print(days[6])
elif d == 7:
    print(days[7])
# another solution
week = ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
day = int(input())
if 0 < day < 8:
    print(week[day-1])
