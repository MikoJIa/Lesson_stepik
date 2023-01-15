# Вводятся вещественные числа в одну строчку через пробел. Необходимо на их основе сформировать множество s.
# Подсказка: множество можно создать по аналогии со списком:
# list(map(float, <список из строк чисел>))
# Вывести на экран значения множества s в порядке возрастания в одну строчку через пробел, используя команду:
# print(*sorted(s))
# P. S. О функции sorted мы еще будем говорить, а также об операторе *. Пока просто запомните такую возможность
# сортировки и вывода произвольных коллекций на экран.
# Sample Input:
# -5.1 -3.0 7.6 10.3 -4.6 2.78
# Sample Output:
# -5.1 -4.6 -3.0 2.78 7.6 10.3

s = set(map(float, input().split()))
print(*sorted(s))