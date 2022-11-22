# Вводится строка (слаг). Замените в этой строке все подряд идущие дефисы (--, ---, ---- и т.д.) на одинарные (-).
# Результат преобразования строки выведите на экран. Программу реализовать при помощи цикла while.
# Sample Input:
# osnovnye--metody-----slovarey
# Sample Output:
# osnovnye-metody-slovarey


string = input()
while '--' in string:
    string = string.replace('--','-',)
print(string)
# another solution
s, i = input(), 0
while i < len(s)-1:
    if s[i] != '-' or s[i+1] != '-':
        print(s[i], end='')
    i += 1
print(s[-1])