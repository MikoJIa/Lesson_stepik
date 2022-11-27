# cicle for
d = [1, 2, 3, 4, 5]

p = 1
for x in d:
    p *= x
print(p)
# как изменить элементы списка
for i in [0, 1, 2, 3, 4]:
    d[i] = 0
print(d) # [0, 0, 0, 0, 0]
# range

print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(0,2))) # [0, 1]
print(list(range(-1, -5))) # []
print(list(range(-10, -5))) # [-10, -9, -8, -7, -6]
print(list(range(-10, -5, 2))) # [-10, -8, -6]
print(list(range(5, 0, -1))) # [5, 4, 3, 2, 1] ноль не включается
print(list(range(5, -1, -1))) # [5, 4, 3, 2, 1, 0] ноль включительно
# Теперь использование цикла for вместе с range
for i in range(5):
    d[i] = 0
print(d) # [0, 0, 0, 0, 0]
# можно так, какой бы длины список не был функция len() высчитает длинну списка
for i in range(len(d)):
    d[i] = 0
print(d) # [0, 0, 0, 0, 0]
# S = 1/2 + 1/3 + 1/4 + ..... + 1/1000

S = 0
for i in range(2, 1001):
    S += 1/i
print(round(S, 2))


