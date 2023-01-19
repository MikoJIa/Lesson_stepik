# Найти максимальную длинну повторяюшихся элементом в обьекте!!
def length(a):
    count_al = 1
    max_r = 0
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            count_al += 1
            if count_al > max_r:
                max_r = count_al
        if a[i] != a[i + 1]:
            count_al = 1
        continue

    return max_r


res = length(['a', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'b', 'b'])
print(res)
