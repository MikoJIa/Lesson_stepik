# Объявите функцию с именем is_large, которая принимает строку (в качестве аргумента) и возвращает False,
# если длина строки меньше трех символов. Иначе возвращается значение True.
# Вызывать функцию не нужно, только объявить.
# Sample Input:
# Я люблю Python!
# Sample Output:
# True

def is_large(x):
    res = False if len(x) < 3 else True
    return res


a = input()
print(is_large(a))