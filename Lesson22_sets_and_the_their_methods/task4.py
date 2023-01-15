# В ночном клубе фиксируется список гостей. Причем гости могут выходить из помещения, а затем, снова заходить.
# Тогда их имена фиксируются повторно. На вход программы поступает такой список (каждое имя записано с новой строки).
# Требуется подсчитать общее число гостей, которые посетили ночной клуб. Полагается, что гости имеют уникальные имена.
# На экран вывести общее число гостей клуба.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# Мария
# Елена
# Екатерина
# Александр
# Елена
# Мария
# Sample Output:
# 4

lst_in = ['Мария', 'Елена', 'Екатерина', 'Александр', 'Елена', 'Мария']
s = set(lst_in)
print(len(s))