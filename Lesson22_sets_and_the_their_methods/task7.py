# Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел).
# Необходимо выбрать и отобразить на экране уникальные числа, присутствующие и в первом и во втором списках одновременно.
# Результат выведите на экран в виде строки чисел, записанных по возрастанию через пробел, используя команду (здесь s - это множество):
# print(*sorted(s))
#
# P. S. О функции sorted мы еще будем говорить, а также об операторе *. Пока просто запомните такую возможность
# сортировки и вывода произвольных коллекций на экран.
# Sample Input:
# 8 11 12 15 -2
# 4 11 10 15 -5 1 -2
# Sample Output:
# -2 11 15

d = list(map(int, input().split()))
c = list(map(int, input().split()))
s = set(c) & set(d)

print(*sorted(s))

# enother solution

a = input().split()
b = input().split()
print(*sorted(set(a) & set(b)))

