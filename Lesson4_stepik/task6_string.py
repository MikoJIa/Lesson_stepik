# Вводятся два слова (через пробел в одной строке). Длина первого слова меньше второго. Необходимо обрезать второе слово до длины первого
# и отобразить обрезанное слово на экране.
# Sample Input:
# Hello Balakirev
# Sample Output:
# Balak

a, b = map(str, input().split())
length_a = len(a)
length_b = len(b)
print(b[:length_a])