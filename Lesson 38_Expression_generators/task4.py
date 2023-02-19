# Вводится целое положительное число a. Необходимо определить генератор, который бы возвращал модули чисел в диапазоне
# [-a; a], а затем еще один, который бы вычислял кубы чисел (возведение в степень 3), возвращаемых первым генератором.
# Вывести в одну строчку через пробел первые четыре значения. (Полагается, что генератор выдает, как минимум четыре
# значения).
# Sample Input:
# 3
# Sample Output:
# 27 8 1 0


def integer_positive(a):
    res = [abs(x) for x in range(-a, a)]
    res2 = [i ** 3 for i in res[:4]]
    print(*res2)


integer_positive(int(input()))

# another solution


def integer_positive(a):
    res = (abs(x) for x in range(-a, a))
    res2 = (i ** 3 for i in res)
    for i in range(4):
        print(next(res2), end=' ')


integer_positive(int(input()))

# another solution
# решение через декоратор


def integer(b):
    def wrapper(x):
        res = (i ** 3 for i in b(x))
        for i in range(4):
            print(next(res), end=' ')
    return wrapper

@integer
def positive(a):
    res2 = (abs(x) for x in range(-a, a))
    return res2


a = int(input())
positive(a)