# Необходимо написать код  который считывает строку и заменяет в ней группы пробельных символов на символ подчёркивание
# Пример: my file name.txt
# Вывод: my_file_name.txt

s = input()

s_new = s[0]
i = 1
while i < len(s):
    if s[i] != ' ':
        s_new += s[i]
    elif s[i - 1] != ' ':
        s_new += '_'
    i += 1
print(s_new)
# enother solution
s = input()
l = s.split()
s1 = '_'.join(l)
print(s1)