# На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через пробел.
# Необходимо задать функцию с именем get_menu, которая преобразует эту строку в список из слов и возвращает этот список.
#  Сигнатура функции, следующая:
# def get_menu(s): ...
# Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:
# 1. Пункт_1
# 2. Пункт_1
# ...
# N. Пункт_N
# Примените декоратор show_menu к функции get_menu, используя оператор @. Более ничего в программе делать не нужно.
# Сами функции не вызывать.
# Sample Input:
# Главная Добавить Удалить Выйти
# Sample Output:
# 1. Главная
# 2. Добавить
# 3. Удалить
# 4. Выйти

def show_menu(x):
    def func(*args, step=0):
        s = x(*args)
        for i in s:
            if type(s) == list:
                step += 1
            print(f"{step}. {i}")
        return step
    return func
@show_menu
def get_menu(s):
    a = list(s)
    return ''.join(a).split()


lst = str(input())
res = get_menu(lst)

# another solution

def show(f):
    def wropper(s):
        for index, item in enumerate(f(s), start=1):
            print(f"{index}. {item}")
    return wropper


@show
def menu(m):
    return m.split()


lst = str(input())
menu(lst)
