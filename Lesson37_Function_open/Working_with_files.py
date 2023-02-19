# try, except, finally
# try:
#   блок операторов
#   критического кода
# except [исключение]:
#   блок операторов
#   обработки исключения
# finally:
#   блок операторов
#   всегда исполняемых
#   вне зависимости, от
#   возникновения исключения

try:
    with open('my_file.txt', encoding='utf-8') as file:  # Это менеджер контекста который может заменить блок
        for line in file:  # try, finally который у нас находится ниже
            print(line, end='')
    # file = open('my_file.txt', encoding='utf-8')
    # try:   # это на случай если файл был открыт, но произошла ошибка!!!
    #     for line in file:
    #         int(line)
    #         print(line, end='')
    # finally:        # А это для того, чтобы файл был закрыт в любом случае!!!
    #     file.close()
except FileNotFoundError:  # если такая ошибка произошла, то мы выведим сообщение
    print('Невозможно открыть файл')
except:  # этот блок для того, чтобы отлавливать все ошибки кроме FileNotFoundError
    print('Произошла ошибка файла')
    # но на всякий случай пропишем и убедимся что файл был закрыт, прописав флаг finally: file.closed
finally:
    print(file.closed)  # True значет файл был закрыт
