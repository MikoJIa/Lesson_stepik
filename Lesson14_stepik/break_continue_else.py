# оператор break - досрочное завершение цикла
# d = [1, 3, 5, 6, -4]
#
# flFind = False
# i = 0
# while i < len(d):
#     print(i)
#     flFind = d[i] % 2 == 0
#     if flFind:
#         break
#     i += 1
# print(flFind)
# #
#
# flFind = False
# i = 0
# while i < len(d) and d[i] % 2 != 0:
#     i += 1
# flFind = i != len(d)
# print(flFind)

# оператор continue - пропуск одной итерации цикла
# пользователь по очерёдно вводит числа, необходимо сумировать все нечётные числа. Если пользователь введёт ноль программа остановится
# s = 0
# d = 1
# while d != 0:
#     d = int(input('Введите целое число: '))
#     if d % 2 == 0:
#         continue
#     s += d
#     print(f's - {s}')
# else в цикле while выполняется в том случае когда цикл while завершон
# S = 1/2 + 1/3 + 1/4 = 1/10 + ..... + 1/0
S = 0
i = -10

while i < 0:
    if i == 0:
        break
    S += 1/i
    i += 1
else:
    print('Сумма вычисления корректна')
print(S)