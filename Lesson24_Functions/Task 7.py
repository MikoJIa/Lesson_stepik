# Объявите функцию для проверки числа на четность (возвращается True, если переданное число четное и False, если число
# нечетное).
# После объявления функции в цикле необходимо считывать целое числовое значение (функцией input), пока не поступит число
#  1. Если прочитанное значение четное (проверяется с помощью заданной функции), то оно выводится на экран (в столбик,
# то есть, каждое значение с новой строки).
# Sample Input:
# 2
# -4
# 5
# 7
# 10
# 1
# Sample Output:
# 2
# -4
# 10


def foo(x):
    return x % 2 == 0


while True:
    a = int(input())
    if foo(int(a)):
        print(a)
        continue
    if a == 1:
        break

# another solution


def is_even(x):
    return x % 2 == 0


a = int(input())
while a != 1:
    if is_even(a):
        print(a)
    a = int(input())


# another solution

def is_func(x):
    return not x % 2


for i in iter(input, '1'):
    if is_func(i):
        print(i)


# another solution

def func(x):
    return not x % 2

while True:
    num = int(input())
    if num == 1:
        break
    else:
        if func(num):
            print(num)
