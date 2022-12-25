# Тестовый веб-сервер возвращает HTML-страницы по URL-адресам (строкам). На вход программы поступают различные URL-адреса.
# Если адрес пришел впервые, то на экране отобразить строку (без кавычек):
# "HTML-страница для адреса <URL-адрес>"
# Если адрес приходит повторно, то следует взять строку "HTML-страница для адреса <URL-адрес>" из словаря и
# вывести на экран сообщение (без кавычек):
# "Взято из кэша: HTML-страница для адреса <URL-адрес>"
# Сообщения выводить каждое с новой строки.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# ustanovka-i-zapusk-yazyka
# ustanovka-i-poryadok-raboty-pycharm
# peremennyye-operator-prisvaivaniya-tipy-dannykh
# arifmeticheskiye-operatsii
# ustanovka-i-poryadok-raboty-pycharm
# Sample Output:
# HTML-страница для адреса ustanovka-i-zapusk-yazyka
# HTML-страница для адреса ustanovka-i-poryadok-raboty-pycharm
# HTML-страница для адреса peremennyye-operator-prisvaivaniya-tipy-dannykh
# HTML-страница для адреса arifmeticheskiye-operatsii
# Взято из кэша: HTML-страница для адреса ustanovka-i-poryadok-raboty-pycharm

lst_in = ['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm',
          'peremennyye-operator-prisvaivaniya-tipy-dannykh', 'arifmeticheskiye-operatsii',
          'ustanovka-i-poryadok-raboty-pycharm']

lst = [x.split() for x in lst_in]
d = {}
for i in lst:
    key = i[0]
    if key not in d:
        d[key] = i
        print('HTML - страница для адреса', *d[key])
    else:
        print('Взято из кэша: HTML - страница для адреса', *d[key])
# enother solution
D = {}
for row in lst_in:
    if row not in D:
        D[row] = row
        print(f'HTML - страница для адреса {D[row]}')
    else:
        print(f'Взято из кэша: HTML - страница для адреса {D[row]}')
# enother solution
URL_adress = []
URL_word = {'One':'HTML - страница для адреса', 'Duble': 'Взято из кэша: HTML - страница для адреса' }

for url in lst_in:
    count = URL_adress.count(url)
    if count == 0:
        URL_adress.append(url)
        print(URL_word['One'], url)
    if count == 1:
        print(URL_word['Duble'], url)