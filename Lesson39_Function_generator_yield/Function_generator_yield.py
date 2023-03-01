# def find_word(f, word):
#     g_index = 0
#     for line in f:
#         index = 0
#         while index != -1:
#             index = line.find(word, index)
#             if index > -1:
#                 yield g_index + index
#                 index += 1
#
#         g_index += len(line)
#
#
# try:
#     with open('my_file.txt', encoding='utf-8') as file:
#         a = find_word(file, "дядя")
#         print(list(a))
# except FileNotFoundError:
#     print('Файл не найден')
# except:
#     print('Ошибка обработки файла!')
# yield показывает что функция =генератор
# генератор ленивый (lazy), одноразовый, кидает StopIteration при исчерпании
# после выполнения yield встаёт на паузу!!!
def squares():
    print('Generator working...')
    for i in range(0, 11, 2):
        yield i ** 2


def pause():
    print('Generator working...')
    while True:
        print(a)
        yield a


a = 10
gen = pause()
print(next(gen))
a = 20
print(next(gen))

for x in squares():  # for в нутри себя обрабатывает Stopiteretion!!!!
    print(x)
print('=' * 20)


def test():
    yield from [int(x) ** 0.5 for x in range(20)]


for i in test():
    print(round(i, 2), end=' ')