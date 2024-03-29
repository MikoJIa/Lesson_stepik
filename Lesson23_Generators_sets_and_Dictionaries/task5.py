# Вводится список книг книжного магазина в формате:
# <автор 1>:<название 1>
# ...
# <автор N>:<название N>
# Авторы с названиями могут повторяться. Необходимо, используя генераторы, сформировать словарь с именем d вида:
# {'автор 1': {'название 1', 'название 2', ..., 'название M'}, ..., 'автор K': {'название 1', 'название 2', ...,
# 'название S'}}
# То есть, ключами выступают уникальные авторы, а значениями - множества с уникальными названиями книг соответствующего
# автора.
# На экран ничего выводить не нужно, только сформировать словарь обязательно с именем d - он, далее будет проверяться в
# тестах!
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# Пушкин: Сказака о рыбаке и рыбке
# Есенин: Письмо к женщине
# Тургенев: Муму
# Пушкин: Евгений Онегин
# Есенин: Русь
# Sample Output:
# True

lst_in = ['Пушкин: Сказака о рыбаке и рыбке',
          'Есенин: Письмо к женщине',
          'Тургенев: Муму',
          'Пушкин: Евгений Онегин',
          'Есенин: Русь']

lst_in = set(lst_in)
d = {}
for i in lst_in:
    key, value = i.split(': ')
    d[key] = d.get(key, {value}) | {value}

print(d)

# another solution

d = dict()
# D = [(i.split(': ')[0], i.split(': ')[1]) for i in lst_in]
lst_in = [x.split(': ') for x in lst_in]
for i in lst_in:
    x, y = i[0], i[1]
    if x not in d:
        d[x] = {y}
    else:
        d[x].add(y)
print(d)

lst_in = [x.split(':') for x in lst_in]

d = {key[0]: {value[1].lstrip() for value in lst_in if value[0] == key[0]} for key in lst_in}
print(d)
