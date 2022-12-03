# Вводится список в виде целых чисел в одну строку через пробел.
# Необходимо сначала сформировать список на основе введенной строки, а затем, каждое значение этого списка изменить,
#  возведя в квадрат. Отобразить результат на экране в виде строки полученных чисел, записанных через пробел.
# Программу следует реализовать с использованием функции enumerate.
# Sample Input:
# 8 -11 4 3 6
# Sample Output:
# 64 121 16 9 36

n = list(map(int, input().split()))
l = []
for i, item in enumerate(n):
    if n[i] == item:
        l.append(item**2)
print(*l)
# enother solution
for i, item in enumerate(n):
    print(item**2 if n[i] == item else n[i] not in item, end=' ')
# enother solution
for i, item in enumerate(n):
    n[i] = item ** 2
print(*n)