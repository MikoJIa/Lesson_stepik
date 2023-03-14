# Вводятся оценки студента в одну строчку через пробел.
# Необходимо определить, имеется ли в этом списке хотя бы одна оценка ниже тройки.
# Если это так, то вывести на экран строку "отчислен", иначе - "учится".
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# 3 3 3 2 3 3
# Sample Output:
# отчислен


def student_assessment(num: list = int) -> str:
    res = any(map(lambda x: x < 3, num))
    if res:
        return 'отчислен'
    return 'учиться'


st = list(map(int, input().split()))
print(student_assessment(st))