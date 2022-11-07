import math
# В летний лагерь нужно отвести n детей и m вожатых с помощью автобусов. Максимальная вместимость каждого автобуса 20 человек.
# Допишите программу для вычисления минимального числа автобусов, необходимых для перевозки детей вместе с вожатыми.
# Результат выведите в консоль в виде целого числа.
# Sample Input:
# 40 5
# Sample Output:
# 3

n, m = map(int, input('Введите числа через пробел - ').split())
bus_capacity = 20
num_people = (n + m)
num_buses = 0
while num_people > 0:
    if num_people / bus_capacity != 0:
        num_people -= bus_capacity
        num_buses += 1
# bus = (n + m) // 20
# if (n + m) % 20 > 0:
#     bus += 1
# print(bus)
# num_buses = math.ceil(num_people / bus_capacity)
print(num_buses)