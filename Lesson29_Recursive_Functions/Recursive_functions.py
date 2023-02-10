# Рекурсивная функция - это функция, которая вызывает сама себя
# У каждой рекурсивной функции должно быть условие остановки!!!!!!!

def recursive(value):
    print(value)
    if value < 4:
        recursive(value + 1)
    print(value)
recursive(1)

# Факториал натурального числа
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)


res = factorial(6)
print(res, end=' ')

# Другой пример использования рекурсии

F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}

def get_files(path, depth=0):
    for f in path:
        print(' '*depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth + 1)
        else:
            print(' '*(depth + 1), ' '.join(path[f]))


get_files(F)