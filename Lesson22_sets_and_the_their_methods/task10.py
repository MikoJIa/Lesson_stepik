# Вводятся два списка городов каждый с новой строки (в строке названия через пробел).
# Необходимо сравнить их между собой на равенство по уникальным (не повторяющимся) городам.
# Если списки содержат одни и те же уникальные города, то вывести на экран ДА, иначе - НЕТ.
# Sample Input:
# Москва Тверь Уфа Казань Уфа Москва
# Уфа Тверь Москва Казань
# Sample Output:
# ДА

a = list(map(str, input().split()))
b = list(map(str, input().split()))
if set(a) == set(b):
    print('ДА')
else:
    print('НЕТ')

# enother solution

print('ДА' if set(input().split()) == set(input().split()) else 'НЕТ')