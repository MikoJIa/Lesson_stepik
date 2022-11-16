# Вводится слово. Проверить, что в этом слове присутствуют все три буквы: t, h и o (в произвольном порядке).
# Реализовать программу с помощью одного условного оператора. Если проверка проходит, вывести ДА, иначе - НЕТ.
# Sample Input:
# Python
# Sample Output:
# ДА

s = input()
if 'h' in s and 't' in s and 'o' in s:
    print('ДА')
else:
    print('НЕТ')
# another solution
print('ДА' if all(['t' in s, 'h' in s, 'o' in s]) else 'НЕТ')