# Вводится список оценок студента - его ответов у доски по предмету "Информатика" в виде чисел от 2 до 5 в одну строку
# через пробел. Если студент имеет хотя бы одну двойку, то он не допускается до экзамена.
# Определить на основе введенного списка, допущен ли студент. Если допущен, то вывести слово ДОПУЩЕН, иначе - НЕ ДОПУЩЕН.
# При реализации задачи используйте множество для определения наличия двойки.
# Sample Input:
# 3 4 4 5 2 3
# Sample Output:
# НЕ ДОПУЩЕН

s = input().split()
if  '2' in set(s):
    print('НЕ ДОПУЩЕН')
else:
    print('ДОПУЩЕН')

# enother solution

print('НЕ ДОПУЩЕН' if '2' in set(input().split()) else 'ДОПУЩЕН')