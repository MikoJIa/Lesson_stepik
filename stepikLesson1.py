import math
# a, b = 1, 2
# print(a, b)
# a, b = b, a
# print(a, b)
# type = 7
# print(type)

a, b = map(int, input().split())
c = math.sqrt(abs(pow(a, 2) + pow(b, 2)))
print(float(round(c)))

