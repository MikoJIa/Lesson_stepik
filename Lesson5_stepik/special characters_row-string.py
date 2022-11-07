text = 'panda needs\nPython'
print(text) # panda needs
# Python
text = '\tpanda needs\nPython'
print(text) # 	panda needs
# Python вышло с табуляцией
text = 'panda \\needs\\ Python'
print(text) # panda \needs\ Python это действие называется экранироввание обратных слэша против ошибок
# Наприме:
text = 'D:\python\Projects\stepik\text1.py'
print(text) # D:\python\Projects\stepik	ext1.py вот здесь произошла ошибка неверный путь к файлу,
# а если мы сделаем экранирование обратных слэшей, то всё будет в порядке.
text = 'D:\\python\\Projects\\stepik\\text1.py'
print(text) # D:\python\Projects\stepik\text1.py
# экранировать следует и ковычки
text = 'Марка вина \'Ягодка\''
print(text)
# row-string - это сырая строка. Это символ который позволяет игнарировать спец.элементы
text = r'D:\\python\\Projects\\stepik\\text1.py'
print(text) # D:\\python\\Projects\\stepik\\text1.py