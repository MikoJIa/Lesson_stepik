# file = open('my_file.txt', encoding='utf-8')  # Что-бы не было кракозябров нужно указать кодировку
# Как же прочитать этот файл?
# print(file.read(4))
# file.seek(0)  # Метод перемещения по позиции файла
# print(file.read(4))
# # метод tell() возвращает номер позиции
# pos = file.tell()
# print(pos)
# как прочитать первую строку

# print(file.readline(), end='')  # что-бы не было пустой строки между двух текущих строк end=''
# print(file.readline())
# а что бы построчно прочитать весь файл:

# for line in file:
#     print(line, end='')

# сразу все строуи прочесть в строку file.readlines()
#
# s = file.readlines()
# print(s)
#
# file.close()

