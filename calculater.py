def calc(a, b, c):
    try:
        if c == '/' and b == 0:
            res = a / b
            return res
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'

    if c == '/' and a >= b or 0 >= a:
        res = a / b
        return res
    if c == '*':
        res = a * b
        return res
    if c == '-' and a >= b or 0 >= a:
        res = a - b
        return res
    if c == '+':
        res = a + b
        return res
    else:
        return 'Операция неверна'


a = int(input())
b = int(input())
c = input()
print(calc(a, b, c))