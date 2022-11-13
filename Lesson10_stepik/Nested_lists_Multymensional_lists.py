# Одномерный список
line = [1, 7, 6, 11, 3]
# двумерный список
img = [[1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]
# мы можем создать двумерный список иначе Например:
img = [line[:], line[:], line[:], line[:], line[:]]
print(img)
print(img[0])
# как обратится к элементу в вложеном списке Например:
print(img[1][0]) # 1 вот таким образом мы можем обратится к элементу в вовтором списке под нулевым индексом
# давайте заменим второй список на другой
img[1] = [0, 0, 0, 0, 0]
print(img) # [[1, 7, 6, 11, 3], [0, 0, 0, 0, 0], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]
# этот список можно преобразовать более короткой записью Например:
img[1] = [1] * 5
print(img) # [[1, 7, 6, 11, 3], [1, 1, 1, 1, 1], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]
# или
img[1][:] = [2] * 5
print(img) # [[1, 7, 6, 11, 3], [2, 2, 2, 2, 2], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]
# или срез через элемент
img[1][0::2] = [3] * 3
print(img) # [[1, 7, 6, 11, 3], [3, 2, 3, 2, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]
t = [['Люблю', 'тебя', 'Петра', 'творенье'],
     ['Люблю', 'твой', 'строгий', 'стройный', 'вид'],
     ['Невы', 'державное', 'тиченье'],
     ['Береговой', 'её', 'гранит']

]
print(t)
print(t[0]) # ['Люблю', 'тебя', 'Петра', 'творенье']
print(t[0][2]) # Петра
# Мы можем при необходимости слово "Петра" заменить на слово "Питон"
t[0][2] = 'Питон'
print(t[0]) # ['Люблю', 'тебя', 'Питон', 'творенье']
# а можем еще список вложить
t.append(['Твоих', 'оград', 'узор', 'чугунный'])
print(t)
# можем удалить например второй список
del t[1]
print(t) # [['Люблю', 'тебя', 'Питон', 'творенье'], ['Невы', 'державное', 'тиченье'], ['Береговой', 'её', 'гранит'], ['Твоих', 'оград', 'узор', 'чугунный']]
# многомерный список с разными уровнями вложености
A = [[[True, False],[1, 2, 3],], ['матрица', 'вектор']]
print(A) # [[[True, False], [1, 2, 3]], ['матрица', 'вектор']]
# обратимся к первому элементу это у нас двумерный список
print(A[0]) # [[True, False], [1, 2, 3]]
# и что бы обратится к второму списку к первому элемнту нам понадобится три аргумента например:
print(A[0][1][2]) # 3 вот так мы обратились к тройке
# второй элемент
print(A[1]) # ['матрица', 'вектор']
a = [True, [1, 0, ["True", ["Истина", "Ложь"], "False"]], False]
print(a[1][2][1][0])
a = [True, [1, 0, ["True", ["Истина", "Ложь"], "F"]], False]
print(a[1][2][2])
t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]
]
print('дядя' in t[0])
