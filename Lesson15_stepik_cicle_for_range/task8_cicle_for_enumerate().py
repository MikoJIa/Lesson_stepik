# Вводится строка с номером телефона. Ожидается формат ввода:
# +7(xxx)xxx-xx-xx
# где x - это цифра. Размер введенных символов считается верным
# (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя).
# Необходимо проверить, что введенная строка соответствует этому формату. Вывести ДА, если соответствует и НЕТ - в противном случае.
# Sample Input:
# +7(123)456-78-99
# Sample Output:
# ДА
tele = input()
b = sorted(tele)
if 1 < len(tele) <= 16 and ''.join(b[-11:]).isdigit():
    for i in range(len(tele)):
        if tele[0] == '+' and tele[1] == '7' and tele[2]== '(' and tele[6] == ')' and tele[10] == '-' and tele[13] == '-':
            print('ДА')
            break
        else:
            print('НЕТ')
            break
else:
    print('НЕТ')

# another solution
s = '+7(xxx)xxx-xx-xx'
n = input().rjust(len(s))
for i, item in enumerate(n):
    if s[i] == item or s[i] == 'x' and item.isdigit():
        continue
    print('НЕТ')
    break
else:
    print('ДА')
# enother solution
s = '+7(xxx)xxx-xx-xx'
num = input()
count = 0
if len(s) == len(num):
    for i, item in enumerate(num):
        if s[i] == item or s[i] == 'x' and item.isdigit():
            count += 1

print('ДА' if count == 16 else 'НЕТ')

