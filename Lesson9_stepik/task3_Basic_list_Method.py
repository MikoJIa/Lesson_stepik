# В одну строчку через пробел вводятся: имя, отчество и фамилия. Необходимо представить эти данные в виде новой строки в формате: Фамилия И.О.
# (Например, Сергей Михайлович Балакирев -> Балакирев С.М.).
# Sample Input:
# Сергей Михайлович Балакирев
# Sample Output:
# Балакирев С.М.

fio = input().split()
famali = fio[2]
name = fio[0][:1] + '.'
name_2 = fio[1][:1] + '.'
print(f'{famali} {name}{name_2}')
# another solution
print(f"{fio[-1]} {fio[0][0]}.{fio[1][0]}.")