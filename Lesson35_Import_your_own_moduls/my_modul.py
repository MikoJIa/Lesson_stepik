import import_your_own_modules
NAME = 'mymodule'


def floor(x):
    print('Функция floor из модуля mymodule')
    return x


# print(NAME)
if __name__ == '__main__':
    for i in range(5):
        print(NAME)