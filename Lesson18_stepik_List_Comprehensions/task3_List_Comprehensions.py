# Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N,
# состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы,
# идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла).
# Результат вывести в виде таблицы чисел как показано в примере ниже.
# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

n = int(input())

l = [([0] * n) for x in range(n)]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][j] == 0:
            l[i][j] = 1
            i+=1
        j+=1
    break

for x in l:
    print(*x)
# enother solution
lst = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
for i in lst:
    print(*i)