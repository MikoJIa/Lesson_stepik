def number_search(lst):
    n = len(lst) + 2
    diff = 0
    for x in range(n + 1):
        diff += x
        d = diff - sum(lst)
    for i in range(1, len(lst) + 1):
        if i not in lst:
            return i, d - i
    return i + 1, i + 2


print(number_search([1, 2, 3, 4, 6]))
