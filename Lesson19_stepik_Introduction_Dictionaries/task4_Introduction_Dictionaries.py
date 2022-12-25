# Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Необходимо на их основе создать словарь d, затем удалить из этого словаря ключи 'False' и '3', если они существуют.
# Ключами и значениями словаря являются строки. Вывести полученный словарь на экран командой:
# print(*sorted(d.items()))
# Sample Input:
# лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина
# Sample Output:
# ('True', 'истина') ('дон', 'река') ('лена', 'имя') ('москва', 'город')

d = dict([i.split('=') for i in input().split()])
[d.pop(x, None) for x in ['False', '3']]
print(*sorted(d.items()))
# enother solution
l = [i.split('=') for i in input().split()]
d = {}
for i in l:
    key, value = i
    d[key] = value
    [d.pop(x, None) for x in ['False', '3']]
print(*sorted(d.items()))
# enother solution
d = dict([i.split('=') for i in input().split()])
key_del = ['False', '3']
for i in key_del:
    if i in d:
        del d[i]
print(*sorted(d.items()))
