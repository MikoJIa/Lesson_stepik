# Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы монеток из своей коллекции.
# Получилось два списка. Эти списки поступают на вход программы в виде двух строк из целых чисел,
# записанных через пробел. Необходимо выделить значения, присутствующие в обоих списках и оставить среди них только
# четные. Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.
# При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.
# Sample Input:
# 1 5 2 7 10 25 50 100
# 5 2 3 7 10 25 55
# Sample Output:
# 2 10

def coins(a, b):
    res = a & b
    return list(sorted(res))


z = set(map(int, input().split()))
c = set(map(int, input().split()))
print(coins(z, c))
res_coins = filter(lambda x: x % 2 == 0, coins(z, c))
for i in res_coins:
    print(i, end=' ')

# another solution

a = list(map(int, input().split()))
b = list(map(int, input().split()))

lst = sorted(filter(lambda x: x in b and x % 2 == 0, a))
print(*lst)

# another solution

a, b = map(str.split, (input(), input()))
print(*filter(lambda a: int(a) % 2 == 0, set(a) & set(b)))