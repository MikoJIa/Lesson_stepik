# Вводятся два натуральных четных числа n и m в одну строчку через пробел, причем n < m.
# Напечатать все нечетные числа из интервала [n, m]. Задачу решить без применения условного оператора.
# Результат вывести на экран в виде строки чисел, записанных через пробел. Программу реализовать при помощи цикла while.
# Sample Input:
# 2 10
# Sample Output:
# 3 5 7 9

n, m = map(int, input().split())
lst = []
while n < m:
    n = (n + 2)
    lst.append(n-1)
print(*lst)
# another solution
n, m = map(int, input().split())
while n < m:
    print(n + (n + 1) % 2, end=' ')
    n += 2
# another solution
start, stop = map(int, input().split())

while start < stop:
    print(start+1, end=' ')
    start += 2
# another solution
n, m = map(int, input().split())
a = []
while n < m:
    n += 1
    a.append(n)

print(*a[::2])