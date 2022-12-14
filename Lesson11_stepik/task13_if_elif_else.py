# Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число).
# По введенным m и n (в одну строку через пробел) определить:
# а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
# б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).
# В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату
# (в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.
# P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
# Sample Input:
# 8 31
# Sample Output:
# 08.30 09.01

days_of_the_month = {1:'01',2:'02',3:'03',4:'04',5:'05',6:'06',7:'07',8:'08',9:'09',10:'10',11:'11',12:'12'}
days = {0:'31', 1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09', 10:'10', 11:'11', 12:'12', 13:'13', 14:'14',
15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20', 21:'21', 22:'22', 23:'23', 24:'24', 25:'25', 26:'26', 27:'27', 28:'28', 29:'29', 30:'30', 31:'31', 32:'01',33:'01'}
year = 366

m, n = map(int, input().split())
if sum(days_of_the_month) != year:
    if  0 < m < 13 and n <= 1:
        print(f'{days_of_the_month[m-1]}.{days[n-1]} {days_of_the_month[m]}.{days[n+1]}')
    elif m == 2 and n == 28:
        print(f'{days_of_the_month[m]}.{days[n-1]} {days_of_the_month[m+1]}.{days[n+4]}')
    elif m in [3,5,4,6,8,9,10,11] and 30 <= n:
        print(f'{days_of_the_month[m]}.{days[n-1]} {days_of_the_month[m+1]}.{days[n+2]}')
    elif m in [3,5,4,6,8,9,10,11] and 0 < n <=29:
        print(f'{days_of_the_month[m]}.{days[n-1]} {days_of_the_month[m]}.{days[n+1]}')
    elif m in [0,1,2,7] and 0 < n <= 30:
        print(f'{days_of_the_month[m]}.{days[n-1]} {days_of_the_month[m]}.{days[n+1]}')
    else:
        if m in [0,1,2,7] and 31 <= n < 33:
            print(f'{days_of_the_month[m]}.{days[n-1]} {days_of_the_month[m+1]}.{days[n+1]}')
# another solution
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mounth, day = map(int, input().split())
if day == 1:
    prev_day = days[mounth - 1]
    prev_mounth = mounth - 1
else:
    prev_day = day - 1
    prev_mounth = mounth
if day == days[mounth - 1]:
    next_day = 1
    next_mounth = mounth + 1
else:
    next_day = day + 1
    next_mounth = mounth
print(f'{prev_mounth:02}.{prev_day:02} {next_mounth:02}.{next_day:02}')
# another solution
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, n = map(int, input().split())
if n == 1:
    print(f'{m - 1:02}.{days[m - 1]:02} {m:02}.{n + 1:02}')
elif n == days[m-1]:
    print(f'{m:02}.{n - 1:02} {m+1:02}.01')
else:
    print(f'{m:02}.{n - 1:02} {m:02}.{n + 1:02}')
