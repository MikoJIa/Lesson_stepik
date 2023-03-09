# list.sort() - метод для сортировки элементов списка
# sorted() - функция для сортировки итерируемых объектов
# сортируем по значения их элементов
a = [4, 3, -10, 1, 7, 12]
b = sorted(a)
print(b)  # [-10, 1, 3, 4, 7, 12]


def id_odd(x):
    return x % 2


a = [4, 3, -10, 1, 7, 12]
b = sorted(a, key=id_odd)
print(b)  # [4, -10, 12, 3, 1, 7]
# можно тот же вариант записать иначе
b = sorted(a, key=lambda x: x % 2)
print(b)  # [4, -10, 12, 3, 1, 7]
# ещё можно через sort()
a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x % 2)
print(a)  # [4, -10, 12, 3, 1, 7]


# а теперь отсортируем по возрастанию


def key_sort(x):
    return x if x % 2 == 0 else 100 + x


a = [4, 3, -10, 1, 7, 12]
b = sorted(a, key=key_sort)
print(b)
# сортировка по последнему символу строки
lst = ['Минск', 'Гомель', 'Брест', 'Могилёв', 'Витебск']
b = sorted(lst, key=lambda x: x[-1])
print(b)  # ['Могилёв', 'Минск', 'Витебск', 'Брест', 'Гомель']
# Необходимо отсортировать по последнему значению по цене
books = (
    ('Евгений Онегин', 'Пушкин А.С', 200),
    ('Муму', 'Тургенев И.С', 250),
    ('Масткр и Маргарита', 'Булгаков М.А', 500),
    ('Мёртвые души', 'Гоголь Н.В', 190)
)

b = sorted(books, key=lambda x: x[-1])
print(b)  # [('Мёртвые души', 'Гоголь Н.В', 190),
          # ('Евгений Онегин', 'Пушкин А.С', 200),
          # ('Муму', 'Тургенев И.С', 250),
          # ('Масткр и Маргарита', 'Булгаков М.А', 500)]