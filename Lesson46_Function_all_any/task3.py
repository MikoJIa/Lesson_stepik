# Объявить функцию с именем is_string, на вход которой поступает коллекция (список, кортеж, множество).
# Она должна возвращать True, если все элементы коллекции строки и False - в противном случае.
# Сигнатура функции должна быть, следующей:
# def is_string(lst): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# Sample Output:
# True

def is_string(collection: str) -> bool:
    res = all(map(lambda x: type(x) == str, collection))
    return res


l = ['weqw', 'weqeq']
print(is_string(l))

# another solution

def is_string2(collection):
    return all(map(lambda x: isinstance(x, str), collection))


print(is_string2(l))


# another solution

def is_string3(collection: str) -> bool:
    new_lst = []
    for item in collection:
        if type(item) == str:
            new_lst.append(True)
        else:
            new_lst.append(False)
    return all(new_lst)


print(is_string3(l))