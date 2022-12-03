# Вводится список в виде целых чисел в одну строку через пробел. Сначала нужно сформировать список из введенной строки.
# Затем, каждый элемент этого списка продублировать один раз.
# Результат отобразить на экране в виде строки полученных чисел, записанных через пробел.
# Sample Input:
# 8 11 2
# Sample Output:
# 8 8 11 11 2 2

n = list(map(int, input().split()))

l = []
for i, item in enumerate(n):
    if item in n :
        l.append(n[i])
        l.append(item)
print(*l)
# enother solution
for i in n:
    print(i, i, end=' ')
# enother solution
for i, item in enumerate(n):
    print(n[i], item, end=' ')
