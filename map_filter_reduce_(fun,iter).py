from functools import reduce

input_list = [2, 3, 4, 5, 6]
# map(fun, iter)

def square(x):
    return x*x
print(list(map(square, input_list))) # [4, 9, 16, 25, 36]

result = map(lambda x: x * x, input_list)
print(list(result)) # [4, 9, 16, 25, 36]


# filter(fun, iter) Используется для отбора значений по условию fun из итерируемого объекта iter:
input_list_2 = [2, 3, 4, 5, 10, 12, 14]
def less_then_10(x):
    if x < 10:
        return x
                        # fun           iter
print(list(filter(less_then_10, input_list_2))) # [2, 3, 4, 5]

# С lambda function:
                            # fun       iter
print(list(filter(lambda x: x < 10, input_list_2))) # [2, 3, 4, 5]

#reduce(fun, iter) применяет fun итеративно ко всем значениям iter и вщзвращяет только одно значение:



input_list_3 = [1, 2, 3, 4, 5]

def addition(x, y):
    return x + y
#                 #fun        iter
print(reduce(addition, input_list_3)) #15
                        # fun       iter
print(reduce(lambda x, y: x + y, input_list_3)) # 15