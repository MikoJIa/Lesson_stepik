# Известно, что порядок нот, следующий: до, ре, ми, фа, соль, ля, си. На вход программы поступает строка с набором этих
# нот, записанных через пробел. Необходимо сформировать список из входной строки с нотами, отсортированными указанным
# образом. Результат вывести в виде строки из нот, записанными через пробел.
# Sample Input:
# до фа соль до ре фа ля си
# Sample Output:
# до до ре фа фа соль ля си

# l = input().split()
# s = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# print(*sorted(l, key=lambda x: s.index(x)))


def func(x):
    s = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
    res_sorted = sorted(x, key=lambda l: s.index(l))
    return res_sorted


print(*func(input().split()))

# another solution

def func2(x):
    s = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
    res = {s[key]: key+1 for key in range(len(s))}
    sort_res = sorted(x, key=lambda c: res[c])
    return sort_res


print(*func2(input().split()))