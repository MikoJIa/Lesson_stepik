# Вводится слово. Необходимо первую букву этого слова сделать заглавной, а остальные - малыми. Результат отобразить на экране.
# Sample Input:
# HELLO
# Sample Output:
# Hello

f = input()
print(f.capitalize())
print(f[0].upper() + f[1:].lower())