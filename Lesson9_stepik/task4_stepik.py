# Вводятся целые числа в одну строчку через пробел (не менее четырех). Необходимо найти три наименьших числа в этой
# последовательности чисел и вывести их на экран в порядке возрастания. Реализовать программу без использования условного оператора.
# Sample Input:
# 8 11 -5 10 -1 0 7
# Sample Output:
# -5 -1 0

s = list(map(int, input().split()))
s.sort()
min1 = []
min1.append(min(s))
s.pop(0)
min1.append(min(s))
s.pop(0)
min1.append(min(s))
print(*min1)
