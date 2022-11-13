# if - уловный оператор
x = -4
if x < 0:
    x = -x
print(x)

# a = float(input('a: '))
# b = float(input('b: '))
# if a < b:
#     a, b = b, a
# print(a, b)

# x = int(input())
#
# if x >= -4 and x <= 10:
#     print('x  в диапазоне [-4; 10]')

marks = [3, 3, 4, 4, 4]

if 2 in marks:
    print('Студент будет отчислен')
else:
    print('Студент успешно сдал сессию')

x = int(input())

if x < 0:
    print('х - отрицательное число')
else:
    print('x - не отрицательное число')