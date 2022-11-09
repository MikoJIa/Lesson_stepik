s = 'hello python'
print(len(s))
print(s[len(s) - 1])
print(s[-1])
print('panda'[3])
print('hello python'[4])
# Срезы строк
print(s[1:3])
print(s[:5])
print(s[6:])
print(s[2:10:2]) #lopt
print(s[1::3]) # eoyo
print(s[:5:3]) # hl
print(s[:6:2]) # hlo
print(s[::2]) # hlopto
print(s[::-1]) # nohtyp olleh
print(s[::-2]) # nhy le
print(s[-3:])
# Стоки неизменяемый тип данных, но мы можем переписать строку с добавлением символов 'Модификация(изменение)'
s1 = 'H' + s[1:]
print(s1)
s1 = 'H' + s[1:5], 'P' + s[7:] # ('Hello', 'Python') заглавные буквы были маленькие стали Большие благодоря срезу и конкатенации
print(s1)
# Из введенной строки отобразить первые пять символов в обратном порядке. Полагается, что введенная строка имеет минимум пять символов.
# a = str(input())[0:5]
# print(a[::-1]) # olleh
# Основные методы строк!!!!!!!
s = 'Python' # s - это обьект
# метод
s.upper()
print(s) # 'Python' не преобразовывает строку в верхний регистр
res = s.upper()
print(res) # 'PYTHON' вот теперь преобразовывает!!!
# метод lower()
print(res.lower()) # 'python' преобразовывает в нижний регистр
# метод count(sub[,start[,end]]) start - индекс с которого начинается поиск, end - индекс которым заканчивается поиск
# sub - это число повторений строки в подстроке.
msg = 'abracadabra'
# msg - аргу.| count() - метод | 'ra'- искомый элемент| 4 - индекс с которого начинаем искать| 10 - инд. котор. заканч.поиск
print(msg.count('ra', 4, 11))
# метод find(sub,[start,[end]]) возвращяет индекс подстроки.
print(msg.find('br')) # 1 начинается с первого индекса
print(msg.find('br', 2, 10)) # 8 начинается от восьмого индекса
# метод rfind(sub,[start[,end]]) обратный поиск
print(msg.rfind('br')) # index 8
# метод index(sub,[start[,end]]) работает обсалютно аналогично методу find(sub,[start,[end]]) есть одно отличие если искомой строки
# несуществует то метод index возвращяет ошибку.
# метод replace(old, new, count=-1) выполняет замену подстрок old на новую подстроку new count=-1 - это замена без ограничений
# например, заменим в нашей строке msg 'a' на 'o'
print(msg.replace('a', 'o')) # obrocodobro
print(msg.replace('ab', 'AB')) # ABracadABra
print(msg.replace('ab', '')) # удаляем все ab на пустую строку output: racadra
print(msg.replace('a', 'o', 2)) # третий параметр это сколько замен мы хотим совершить output: obrocadabra
# метод isalpha() возвращяет истину True если строка целиком состоит из букв, если букв нет то Foals
print(msg.isalpha()) # True
print('hello world'.isalpha()) # False всё по тому что в стоке есть пробел, а пробел это не буква
# метод isdigit() проверяет строку на числа. True будет в том случае если в стоке все элементы это числа
print('5.6'.isdigit()) # False в строке есть элемент который не является числом '.'
print('6457623'.isdigit()) # True в строке все числа
# метод rjust(width[,fillchar='']) возвращяет новую сроку, с заданным числом символов width-ширина
# fillchar -заполняющий элементы
e = 'abc'
print(e.rjust(5)) #'  abc' теперь строка состоит из пяти символов, для этого добовляется два пробела
# Например, если мы хотим перед числом 12 добавить два 0.
d = '12'
print(d.rjust(4, '0')) #0012 строка теперь состоит из 4 символов и перед число 12 два нуля
# метод ljust(width,[fillchar='']) обсалютно идентично методу rjust(width[,fillchar='']) толко добовляет элем. с конца
print(d.ljust(10, '*')) # 12********
# метод split(sep=None, maxsplit=-1), sep-фрагмент разбиение строки
print('Иванов Иван Иванович'.split(' ')) # ['Иванов', 'Иван', 'Иванович'] мы получае список из строк
digs = '1, 2,3, 4,5'
print(digs.split(',')) #['1', ' 2', '3', ' 4', '5']
print(digs.replace(' ', '').split(',')) # ['1', '2', '3', '4', '5'] так мы удалили лишние пробелы
# метод .join(список) из списка строк собирает единую строку
d = digs.replace(' ', '').split(',') # replace() возвращает строку str, split()преобразует в список list
print(', '.join(d)) # 1, 2, 3, 4, 5 теперь из списка мы получаем числа  и тип 'str'
fio = 'Иванов Иван Иванович'
print(', '.join(fio.split())) # Иванов, Иван, Иванович мы за счет метода split() добавили запетые к пробелам
# а еслибы небыло бы метода split() получилось бы вот так: И, в, а, н, о, в,  , И, в, а, н,  , И, в, а, н, о, в, и, ч
# метод strip() удаляет все символы пробелов и переносов строк в начале и в конце строки.
print('    hello world      \n'.strip()) # hello world
# метод rstrip() удаляет от зада
print('    hello world      \n'.rstrip()) # '    hello world'
# метод lstrip() удаляет с переди символы
print('    hello world      \n'.lstrip()) # 'hello world     \n'
f = input()
print(f[0].upper() + f[1:].lower())

#Напишите программу ввода двух слов через пробел. Сформируйте новую строку, продублировав первое слово дважды, а второе - трижды
# (все слова в результирующей строке должны идти через пробел). Результат выведите на экран.
# Программу следует реализовать без использования F-строк, а с применением оператора дублирования строк.
# Sample Input:
# hello python
# Sample Output:
# hello hello python python python

# a, c = map(str, input().split())
# str_1 = ((a + ' ') * 2).rstrip()
# str_2 = ((c + ' ') * 3).rstrip()
# print(str_1 + ' ' + str_2)
# Можно через список
# s = input().split()
# print((s[0] + ' ')*2 + (s[1] + ' ')*3)
