# Вводится целое число k (1 <= k <= 365).
# Определить, каким днем недели (понедельник, вторник, среда, четверг, пятница, суббота или воскресенье)
# является k-й день не високосного года, в котором 1 января является понедельником.
# Sample Input:
# 121
# Sample Output:
# вторник
k = int(input())
day = 365
mondey = list([i for i in range(1, 366, 7)])
if k in mondey:
    print('понедельник')
tuesday = list([i for i in range(2, 366, 7)])
if k in tuesday:
    print('вторник')
wednesday = list([i for i in range(3, 366, 7)])
if k in wednesday:
    print('среда')
thursday = list([i for i in range(4, 366, 7)])
if k in thursday:
    print('четверг')
friday = list([i for i in range(5, 366, 7)])
if k in friday:
    print('пятница')
saturday = list([i for i in range(6, 366, 7)])
if k in saturday:
    print('суббота')
sunday = list([i for i in range(7, 366, 7)])
if k in sunday:
    print('воскресенье')
# another solution
k = int(input())
weeks = ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
print(weeks[k % 7 - 1])