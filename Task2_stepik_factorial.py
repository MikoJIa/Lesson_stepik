from math import factorial as f
# Допишите программу для нахождения числа сочетаний из n по k (значения вводятся в программе), используя формулу
# ., где . Выведите результат в консоль в виде целого числа с помощью функции print.
# Для вычисления факториалов воспользуйтесь соответствующей функцией из библиотеки math.
# Sample Input:
# 6 3
# Sample Output:
# 20

n, k = map(int, input('Введите два числа через пробел - ').split())
# fact_n = math.factorial(n)
# fact_k = math.factorial(k)
# diff_n_k = math.factorial(n - k)
# combi_num = fact_n / (fact_k * diff_n_k)
combi_num = f(n) / (f(k) * f(n - k))
print(int(combi_num))
