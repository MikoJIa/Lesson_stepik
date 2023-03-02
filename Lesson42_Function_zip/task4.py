# Вводится строка из слов, записанных через пробел. Необходимо на их основе составить прямоугольную таблицу из трех
# столбцов и N строк (число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить.
# Реализовать эту программу с использованием функции zip. Результат отобразить на экране в виде прямоугольной таблицы из
# слов, записанных через пробел (в каждой строчке).
# Sample Input:
# Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь
# Sample Output:
# Москва Уфа Тула
# Самара Омск Воронеж
# Владивосток Лондон Калининград


def zip_city(x):
    for i in (x, x, x):

        return i


city = iter(input().split())
res = zip_city(city)
for _ in range(3):
    print(next(res), next(res), next(res))

# another solution

for row in zip(*[iter(input().split())] * 3):
    print(*row)

# another solution

s = iter(input().split())
for x in zip(s, s, s):
    print(' '.join(x))

# another solution

def grouper(iterabl, n):
    return zip(*[iter(iterabl)] * n)


for group in grouper(input().split(), 3):
    print(*group)