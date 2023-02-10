# На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию get_list,
# которая преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для этой функции,
# который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:
# print(*lst)
# Sample Input:
# 8 11 -5 4 3 10
# Sample Output:
# -5 3 4 8 10 11


def get_list(x):
    def func(z):
        s = [int(i) for i in x(z)]
        s = sorted(s)
        return s
    return func
@get_list
def get_menu(a):
    return a.split()


ls = input()
lst = get_menu(ls)
print(*lst)

# another solution

def show(x):
    return lambda *args, **kwargs: sorted(x(*args, **kwargs))

@show
def menu(a):
    return list(map(int, a.split()))


ls = input()
lst = menu(ls)
print(lst)