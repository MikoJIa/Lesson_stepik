# (Для учебных целей). Вводится строка. Необходимо в ней заменить кириллические символы на соответствующие латинские
# обозначения (без учета регистра букв), а все остальные символы - на символ дефиса (-). Для этого в программе определен
#  словарь (см. листинг). Используя его, запишите функцию map, которая бы выдавала преобразованные фрагменты для входной
#  строки. На основе этой функции сформируйте строку, состоящую из преобразованных фрагментов (фрагменты в строке должны
#  идти друг за другом без пробелов). Отобразите результат на экране.
# Sample Input:
# Привет Питон
# Sample Output:
# privet-piton

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

l = ''.join(map(str, input().lower()))


def func(x):
    s = []
    morze = {k: v for k, v in t.items()}
    for i in x:
        if i in morze:
            s.append(morze[i])
        elif i == ' ':
            s.append('-')
    return s


res = func(l)
print(''.join(res))

# another solution

translit = map(lambda x: t.get(x.lower(), '-'), input())
print(''.join(translit))

# another solution

text = ''.join(map(lambda x: t[x] if x in t else '-', input().lower()))
print(text)

# another solution

def che(c):
    if c in t:
        return t[c]
    else:
        return "-"

res=''.join(map(che, input().lower()))
print(res)