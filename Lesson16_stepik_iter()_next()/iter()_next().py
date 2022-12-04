# Встроеный итератер iter
d = [3, 5, 7, 10, 32]
iter(d)
# необходимо создать для итератера переменную
it = iter(d)
print(next(it)) # 3
print(next(it)) # 5
print(next(it)) # 7
print(next(it)) # 10

r = range(5)
f = iter(r)
print(next(f)) # 0
print(next(f)) # 1
print(next(f)) # 2
print(next(f)) # 3
print(next(f)) # 4
print(next(f)) # Traceback (most recent call last): StopIteration

