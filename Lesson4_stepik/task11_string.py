# Вводится строка, состоящая из слов, разделенных пробелом.
# Необходимо подсчитать число слов в этой строке и результат (число) отобразить на экране.
# Sample Input:
# I love Python
# Sample Output:
# 3
s = input()
d = s.split()
count = 0
for i in d:
    if i in d:
        count += 1
print(count)
# the second solution
print(len(s.split()))
# the third solution
print(s.count(' ') + 1)
