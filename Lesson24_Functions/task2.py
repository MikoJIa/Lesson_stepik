# Объявите функцию с двумя параметрами width и height (ширина и высота прямоугольника), которая выводит сообщение
# (без кавычек):
# "Периметр прямоугольника, равен x"
#
# где x - вычисленный периметр прямоугольника.
# После объявления функции прочитайте (с помощью функции input) два целых числа, записанных в одну строку через пробел,
#  и вызовите функцию с этими значениями.
# Sample Input:
# 8 11
# Sample Output:
# Периметр прямоугольника, равен 38

def per_rectangle(width, height):
    x = 2 * (width + height)
    print(f'Периметр прямоугольника, равен {x}')

one = list(map(int, input().split()))
per_rectangle(one[0], one[1])

# another solution

def rectangle(width, height):
    x = 2 * (width + height)
    print(f'Периметр прямоугольника, равен {x}')


a, b = map(int, input().split())
rectangle(a, b)