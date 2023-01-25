# Объявите функцию, которая принимает строку (в качестве аргумента) и возвращает False,
# если длина строки меньше 6 символов. Иначе возвращается значение True.
# После объявления функции прочитайте (с помощью функции input) список названий городов,
# записанных в одну строку через пробел. Затем, используя генератор списка и созданную функцию,
# сформируйте список из названий городов длиной не менее шести символов на основе введенного исходного списка.
# Результат отобразите на экране командой:
# print(*lst)
# где lst - итоговый сформированный список.
# Sample Input:
#
# Москва Уфа Пермь Самара Вологда
# Sample Output:
#
# Москва Самара Вологда

def function(string):
    if len(string) >= 6:
        return True
    else:
        return False


st = input().split()
lst = [i for i in st if function(i)]
print(*lst)

# another solution


def func(x):
    return True if len(x) >= 6 else False


st2 = input().split()
lst2 = [i for i in st2 if func(i)]
print(*lst2)


# another solution


def foo(a):
    return len(a) >= 6


lst3 = [i for i in input().split() if foo(i)]
print(*lst3)


