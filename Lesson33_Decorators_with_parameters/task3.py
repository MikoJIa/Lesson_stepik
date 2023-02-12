# Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий словарь
# для замены русских букв на соответствующее латинское написание:
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в нижний
# регистр - малые буквы).
# Определите декоратор с параметром chars и начальным значением " !?", который данные символы преобразует в символ "-" и
# , кроме того, все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису.
# Полученный результат должен возвращаться в виде строки.
# Примените декоратор с аргументом chars="?!:;,. " к функции и вызовите декорированную функцию для введенной строки s:
# s = input()
# Результат отобразите на экране.
# Sample Input:
# Декораторы - это круто!
# Sample Output:
# dekoratory-eto-kruto-


def dec_func(chars=" !?"):
    def func(x):
        def wrapper(*args):
            f = x(*args)
            d = ''
            for i in f:
                if i in chars:
                    d += '-'
                else:
                    d += i
            while d.count('---') != 0 or d.count('--') != 0:
                    d = d.replace('---', '-').replace('--', '-')
            return d

        return wrapper
    return func


@dec_func(chars='?!:;,. ')
def main(a):
    a = a.lower()
    st = ''
    for i in range(len(a)):
        if a[i] in t:
            st += t[a[i]]
        else:
            st += a[i]

    return st


s = input()
print(main(s))


# another solution

def set_chars(chars=' !?'):
    def decor_str(x):
        def wrapper(*args):
            b = ''
            for i in x(*args):
                b += '-' if i in chars else i
                b = b.replace('--', '-')
            return b
        return wrapper
    return decor_str


@set_chars('?!:;,. ')
def get_str(s):
    return ''.join([t[i] if i in t else i for i in s.lower()])


s = input()
print(get_str(s))