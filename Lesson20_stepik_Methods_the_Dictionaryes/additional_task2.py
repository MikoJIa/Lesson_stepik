# Необходимо написать код который будет принимать на вход строку в стиле underscore, нужно переделать эту строку в стиль
# UpperCamelCase
# Например: my_first_class
# Вывод: MyFirstClass

s = input()

f = [x.capitalize() for x in s.split('_')]
print(''.join(f))
