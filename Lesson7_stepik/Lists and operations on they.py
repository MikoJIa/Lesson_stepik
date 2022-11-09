''''Список это упорядоченная коллекция данных'''
city = ['Москва', 'Тверь', 'Вологда', [1,2,3]]

print(city)
# Следует найти средний балл по оценкам!!
marks = [2, 3, 4, 3, 5, 2]
print((marks[0] + marks[1] + marks[2] + marks[3] + marks[4] + marks[5]) / 6)
# можно в ручную создать список
# Например:
t = [23.5, 24.6, 25.8, 27.0, 28.5]
print(round(sum(t) / len(t), 2))
print(list('Python')) # ['P', 'y', 't', 'h', 'o', 'n']
s = list('Python')
print(max(s))
print(min(s))
print(sorted(s))
# Функция Len() определения числа элементов в списке(длина списка)
print(len(marks))
# Функция max() для нахождения максимального числа в списке
print(max(marks))
# Функция min() для нахождения минимального числа в списке
print(min(marks))
# Функция sum() для вычисления суммы
print(sum(marks))
# Функция sorted() для сортировки коллекции
print(sorted(marks)) # [2, 2, 3, 3, 4, 5]
# сортировка в обратном напровлении
print(sorted(marks, reverse=True)) # [5, 4, 3, 3, 2, 2]
# Функция

print([1,2,3] + [4,5])# [1, 2, 3, 4, 5]
print('Москва' in city)# True
# Можно проверить на вложенный список
print([1,2,3] in city)
# Теперь вложим в ручную список в список
print([1,2,3] in city)
del city[2]
print(city)