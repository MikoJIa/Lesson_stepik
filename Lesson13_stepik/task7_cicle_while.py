# Последовательность Фибоначчи образуется так: первые два числа равны 1 и 1, а каждое последующее равно сумме двух предыдущих.
# Имеем такую последовательность чисел: 1, 1, 2, 3, 5, 8, 13, ...
# Постройте последовательность Фибоначчи длиной n (n вводится с клавиатуры).
# Результат отобразите в виде строки полученных чисел, записанных через пробел. Программу реализовать при помощи цикла while.
# Sample Input:
# 8
# Sample Output:
# 1 1 2 3 5 8 13 21


n = int(input())
fib2 = fib1 = 1
lst = [1, ]
i = 1
while i < n:
    fib1, fib2 = fib2, fib1 + fib2
    lst.append(fib1)
    i += 1
print(*lst)
# another solution
f1 = 1
f2 = 1
n = int(input())
print(f1,f2, end=' ')

while n > 2:
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
    n -= 1
# another solution
n = int(input())
fib = [1,1]
while len(fib) < n:
    fib.append(sum(fib[-2:]))
print(*fib)
