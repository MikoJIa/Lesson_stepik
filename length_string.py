#Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, которая подсчитывает количество слов в этой строке.
# Формат входных данных
# На вход программе подается строка.
# Формат выходных данных
# Программа должна вывести количество слов в строке.
# Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько)
# Примечание 2. Решите задачу в одну строчку кода 😎.
# Sample Input 3:
# The future belongs to those who believe in beauty of their dreams
# Sample Output 3:
# 12

print(len(list(filter(lambda x: x != ' ', input().split()))))


def func(string: str) -> int:
    result = string.split()
    return len(result)


print(func('Решите задачу в одну строчку кода'))

