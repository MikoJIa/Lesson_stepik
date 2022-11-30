# Вводится строка. Необходимо найти все индексы фрагмента "ра" во введенной строке.
# Вывести в строку через пробелы найденные индексы. Если этот фрагмент ни разу не будет найден, то вывести значение -1.
# Sample Input:
# Барабанщик бил бой в барабан
# Sample Output:
# 2 23

s = input()
if 'ра' not in s:
    print(-1)
else:
    for i in range(0, len(s)):
        if s[i] == 'р' and s[i + 1] == 'а':
            print(i,end=' ')
# enother solution
s = input().lower()
count = 0

for i in range(len(s) - 1):
	if s[i] + s[i +1] == 'ра':
		count += 1
		print(i, end=' ')
if count == 0:
	print(-1)
# enother solution
string = input().lower()

if 'ра' in string:
    for index, value in enumerate(string):
        if string[index:index+2] == 'ра':
            print(index, end=' ')
else:
    print(-1)
# enother solution
s = input()
res = [i for i in range(len(s) - 1) if s[i] == 'р' and s[i + 1] == 'а']
print(*res or [-1])

