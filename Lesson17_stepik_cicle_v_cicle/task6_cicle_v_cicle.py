# Вводится список целых чисел в одну строку через пробел. Необходимо выполнить его сортировку выбором по возрастанию (неубыванию).
# Идея алгоритма очень проста и проиллюстрирована на рисунке ниже.
#
#
# Вначале мы рассматриваем первый элемент списка и ищем второй минимальный относительно первого элемента (включая и его).
# На рисунке - это последний элемент со значением -1. Затем, меняем местами первый и последний элементы.
# Переходим ко второму элементу списка и повторяем эту же процедуру, но относительно второго элемента
# (то есть, первый уже не рассматриваем). На рисунке минимальный элемент - это 2, поэтому менять местами здесь ничего не нужно.
# Переходим к 3-му элементы со значением 6. Относительно него находим минимальный элемент - это 3. Меняем их местами.
# Вот идея алгоритма сортировки выбором. Реализуйте его для вводимого списка целых чисел.
# Результат выведите в виде списка чисел одну строку через пробел.
# Sample Input:
# 8 11 -53 2 10 11
# Sample Output:
# -53 2 8 10 11 11

lst = list(map(int, input().split()))

for i in range(0, len(lst)):
    smallest = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[smallest]:
            smallest = j
    lst[i], lst[smallest] = lst[smallest], lst[i]

print(*lst)
# enother solution
# x = list(map(int,input().split()))
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i] <= x[j]:
#             continue
#         else:
#             x[i],x[j] = x[j],x[i]
# print(*x)
# # enother solution
# l = list(map(int, input().split()))
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i] < l[j]:
#             l[i], l[j] = l[j], l[i]
# print(*l)
# # enother solution
# n = list(map(int, input().split()))
# s = []
# for i in range(len(n)):
#     s.append(min(n))
#     n.remove(min(n))
# print(*s)
# enother solution
n = list(map(int, input().split()))
for i in range(len(n)):
    for j, item in enumerate(n[:len(n)-i]):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]
print(*n)












