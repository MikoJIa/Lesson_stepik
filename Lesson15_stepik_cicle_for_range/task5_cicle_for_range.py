# Вводится список названий городов в одну строчку через пробел.
# Перебрать все эти названия с помощью цикла for и определить,
# начинается ли название следующего города на последнюю букву предыдущего города в списке.
# Если последними встречаются буквы 'ь', 'ъ', 'ы', то берется следующая с конца буква.
# Вывести на экран ДА, если последовательность удовлетворяет этому правилу и НЕТ - в противном случае.
# Sample Input:
# Москва Астрахань Новгород Димитровград Душанбе
# Sample Output:
# ДА

city = list(map(str, input().lower().split()))

mark = ['ь', 'ъ', 'ы']
out = 'ДА'
for i in range(len(city) - 1):
    if city[i][-1] in mark:
        if city[i+1][0] == city[i][-2]:
            print('ДА')
            break
    else:
        if city[i+1][0] != city[i][-1]:
            print('НЕТ')
            break
# enother solution
data = input().lower().split()
result = 'ДА'
for i in range(1, len(data)):
    if data[i][0] != data[i - 1].rstrip("ьъы")[-1]:
        result = 'НЕТ'
print(result)
# enother solution
lst = [city.rstrip("ьъы") for city in input().split()]
for i in range(1,len(lst)):
    if lst[i-1][-1] != lst[i][0].lower():
        print("НЕТ")
        break
else:
    print("ДА")
