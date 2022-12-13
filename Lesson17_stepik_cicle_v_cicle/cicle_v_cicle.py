for i in range(1, 4):
    for j in range(1, 6):
        print(f'i = {i}, j = {j}', end=' ')
    print() # для того чтобы перевести курсор на новую строку
# неоходимо сложить все элементы первого списка с элементами второго списка
a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
c = []
for i, row in enumerate(a):
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j])
    c.append(r)
print(c)
# необходимо в списке убрать двойные и более пробелы
t = ['- Скажика,  дядя, ведь не даром',
     'Я Python выучил с  каналом',
     'Балакирев что  раздавал?',
     'Ведь были  ж заданья боевые,',
     'Да, говорят,  ещё какие!',
     'Не даром помнит   вся Россия',
     'Как мы рубили  их тогда']
for i, line in enumerate(t):
    while line.count('  '):
        line = line.replace('  ', ' ')
    t[i] = line
print(t)
# Необходимо с клавиатуры ввести два целых значения M и N это будут размеры двухмерного списка, после чего полученый результат
# списков заменить на еденицы
M, N = list(map(int, input('Введите M и N').split()))

zeros = []
for i in range(M):
    zeros.append([0] * N)
print(zeros) # [[0, 0, 0], [0, 0, 0]]

for i in range(M):
    for j in range(N):
        zeros[i][j] = 1
print(zeros) # [[1, 1, 1], [1, 1, 1]]
# У нас есть двумерный список, необходимо значения строк заменить на значение столбца
# Первый цикл i будет обозначать вертикаль, а второй цикл j горизонталь
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for i in range(len(A)):
    for j in range(i+1, len(A)):
        A[i][j],A[j][i] = A[j][i],A[i][j]

for r in A:
    for x in r:
        print(x, end=' ')
    print() # 1	5	9	13
            # 2	6	10	14
            # 3	7	11	15
            # 4	8	12	16
# Сделать ёлочку из смайликов
smile = '\U0001f600'
for i in range(10):
    count = 0
    emoticons = ''
    while count <= i:
        emoticons += smile
        count += 1
    print(emoticons)
