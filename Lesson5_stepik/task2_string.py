# Вводится слово. Необходимо сформировать новую строку, где введенное слово будет заключено в двойные кавычки. Результат выведите на экран.
# Sample Input:
# language
# Sample Output:
# "language"




s = input()
s1 = '"' + s[0::]
s2 = s1 + '"'
print(s2)
# the second solution
print(s.rjust(len(s) + 1, '\"').ljust(len(s) + 2, '\"'))
# the third solution
print('\"', '\"', sep=input())