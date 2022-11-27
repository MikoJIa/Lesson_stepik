# (На использование цикла while). Вводятся названия книг (каждое с новой строки).
# Удалить из введенного списка все названия, состоящие из двух и более слов (слова в названиях разделяются пробелом).
# Результат вывести на экран в виде строки из оставшихся названий через пробел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки
# Sample Input:
# Муму
# Евгений Онегин
# Сияние
# Мастер и Маргарита
# Пиковая дама
# Колобок
# Sample Output:
# Муму Сияние Колобок


lst_in = ['Муму','Евгений Онегин','Сияние','Мастер и Маргарита','Колобок']
lst = []
i = 0
while i < len(lst_in):
    if ' ' not in lst_in[i]:
        lst.append(lst_in[i])

    i += 1
    if i > len(lst_in):
        break
print(*lst)
# enother solution
i = 0
while i < len(lst_in):
    if ' ' in lst_in[i]:
        lst_in.pop(i)
    else:
        i += 1
print(*lst_in)
# enother solution
n = len(lst_in)
while n:
    n -= 1
    if lst_in[n].count(' '):
        del lst_in[n]
print(*lst_in)