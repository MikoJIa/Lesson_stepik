# На вход программы поступает список наименований рек, записанных в одну строчку через пробел.
# Необходимо отсортировать этот список в порядке убывания длин названий. Результат вывести в одну строчку через пробел.
# Sample Input:
# Лена Енисей Волга Дон
# Sample Output:
# Енисей Волга Лена Дон


def length(z):
    return len(z)


a = list(map(str, input().split()))
print(*sorted(a, key=length, reverse=True))