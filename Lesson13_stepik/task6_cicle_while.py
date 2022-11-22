# Вводится натуральное (то есть, целое положительное) число (от трехзначного и более). Найти произведение всех его цифр.
# Результат вывести на экран. Программу реализовать при помощи цикла while.
# Sample Input:
# 821
# Sample Output:
# 16


n = int(input())
sum = 1
while n != 0:
    last = n % 10
    sum *= last
    n = n // 10
print(sum)
# another solution
summ = 1
while n:
    summ *= n % 10
    n //= 10
print(summ)
# another solution
n, sum = list(map(int, input())), 1
while n:
    sum *= int(n.pop())
print(sum)
# another solution
n = list(map(int, input()))
while len(n) != 1:
    n[0] = n[0] * n[1]
    del n[1]
print(n[0])