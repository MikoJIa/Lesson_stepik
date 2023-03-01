# На вход поступает строка из целых чисел, записанных через пробел. С помощью функции map преобразовать эту строку в
# список целых чисел, взятых по модулю. Сформируйте именно список lst из таких чисел. Отобразите его на экране в виде
# набора чисел, идущих через пробел.
# Sample Input:
# -5 6 8 11 -10 0
# Sample Output:
# 5 6 8 11 10 0

def int_number(x):
    for j in x:
        if j < 0:
            yield abs(j)
        else:
            yield j


a = list(map(int, input().split()))
int_number(a)
for i in int_number(a):
    print(i, end=' ')

# another solution

lst = list(map(lambda x: abs(int(x)), input().split()))
print(*lst)