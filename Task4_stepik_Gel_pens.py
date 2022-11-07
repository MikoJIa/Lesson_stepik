import math
#  Гелевая ручка стоит x рублей. Сегодня магазин предоставляет скидку в 10% на каждую купленную ручку. Какое наибольшее
# количество таких ручек можно будет купить на 500 рублей? Результат выведите в консоль в виде целого числа.
# Sample Input:
# 20
# Sample Output:
# 27

x = int(input())
discount = 10
discount_one_pen = x / 100 * discount
price_one_pen = x - discount_one_pen
num_pens_purchased = math.floor(500 / price_one_pen)
print(num_pens_purchased)
# можно максимально коротко сформировать код!!!!!!!!!!
print(math.floor(500/(x-x/10)))
