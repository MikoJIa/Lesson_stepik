# Функция filter
# filter(func, *iterables) - фильтрация элементов итерированного обьекта

# a = [0] * 10
# n = 0
# x = int(input())
# while n < len(a):
#     for i in range(1, x+1):
#         a[n] = i
#         n += 1
# print(a)

# b = filter(lambda x: x % 2 == 0, a)
# lst = list(b)
# print(lst)
# for x in lst:
#     print(x, end=' ')

def is_prost(x):
    d = x - 1
    if d < 0:
        return False
    while d > 1:
        if x % d == 0:
            return False
        d -= 1

    return True


s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = filter(is_prost, s)
b2 = filter(lambda x: x % 2 != 0, filter(is_prost, s))
print(list(b2))


d = ('Минск', 'Брест1', 'Могилёв', 'Гомель3', 'Витебск')
c = filter(str.isalpha, d)
print(list(c))
