# isinstance(объект, тип данных)
# True - если объект соответствует указанному типу
# False - если не соответствует

a = 5
print(isinstance(a, int))  # True
print(isinstance(a, float))  # False
b = True
print(isinstance(b, bool))  # True
print(isinstance(b, int))  # True
# Если мы хотим проверить более точно
print(type(b) == bool)  # True  или print(type(b) is bool)
print(type(b) == int)  # False  или print(type(b) is int)
print(type(b) in (bool, float, str))  # True
# множественная проверка
c = 5.5
print(isinstance(c, (float, int)))  # True
# или можно записать вот так:
print(isinstance(c, int) or isinstance(c, float))  # True

# в этом кортеже необходимо посчитать сумму только вещественных чисел
data = (4.5, 8.7, True, 'книга', 8, 10, -11, [True, False])




def summ_real_number(x):
    summ = 0
    for i in x:
        if isinstance(i, float):
            summ += i
    return summ


print(summ_real_number(data))  # 13.2

# можно туже задачу решить иным способом

def real_number(x):
    # s = sum(filter(lambda c: isinstance(c, float), x))
    # а что бы проверить целочисленное значение, необходимо воспользоватся функцией type(), так мы проверим точно на
    # целое число, иначе булево значение тоже будет воспринимать как целое число
    s = sum(filter(lambda c: type(c) is int, data))  # 7
    return s


print(real_number(data))  # 13.2