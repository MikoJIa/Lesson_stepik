# Функции из предыдущего подвига 5 добавьте еще один формальный параметр up с начальным булевым значением True.
# Если параметр up равен True, то тег (указанный в формальном параметре tag) следует записывать заглавными буквами,
# а иначе - малыми.
# После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию
# (с выводом результата ее работы на экран):
# - первый раз со строкой и именованным аргументом tag со значением 'div'
# - второй раз со строкой, именованным аргументом tag со значением 'div' и именованным аргументом up со значением False.
# Sample Input:
# Python is best!
# Sample Output:
# <DIV>Python is best!</DIV>
# <div>Python is best!</div>


def get_tag(a, tag='div', up=True):
    if up:
        return f'<{tag.upper()}>{a}</{tag.upper()}>'
    else:
        return f'<{tag}>{a}</{tag}>'


st = input()
print(get_tag(st, tag='div', up=True))
print(get_tag(st, tag='div', up=False))
