# Вводится список в формате:
# <город 1> <численность населения 1> <город 2> <численность населения 2> ... <город N> <численность населения N>
# Необходимо с помощью list comprehension сформировать список lst, содержащий вложенные списки из пар:
# <город> <численность населения>
# Численность населения - целое число в тыс. человек. Вывести результат на экран в виде списка командой:
# print(lst)
# Sample Input:
# Москва 15000 Уфа 1200 Самара 1090 Казань 1300
# Sample Output:
# [['Москва', 15000], ['Уфа', 1200], ['Самара', 1090], ['Казань', 1300]]

n = list(map(str, input().split()))
lst = [[n[i-1], int(n[i])] for i in range(1, len(n), 2)]
print(lst)

# enother solution
lst = list(map(str, input().split()))
s = [[lst[i], int(lst[i + 1])]
     for i in range(len(lst))
     if i % 2 == 0
     ]
print(s)
# enother solution
lst = list(map(str, input().split()))
l1 = lst[::2]
l2 = lst[1::2]
l2 = [int(i) for i in l2]
l3 = [[l1[i], l2[i]] for i in range(len(l1))]
print(l3)