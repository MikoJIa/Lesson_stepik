# Вводятся названия городов в одну строку через пробел. На основе этой строки необходимо создать список lst и добавить его в конец следующего списка:
# cities = ["Москва", "Тверь", "Вологда"]
# Вывести результат на экран командой:
# print(*lst)
# Sample Input:
# Уфа Казань Севастополь
# Sample Output:
# Москва Тверь Вологда Уфа Казань Севастополь

ls = list(map(str, input().split()))
cities = ["Москва", "Тверь", "Вологда"]
lst = (cities + ls)
print(*lst)