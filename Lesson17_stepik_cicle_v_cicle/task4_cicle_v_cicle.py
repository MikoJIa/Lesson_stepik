import numpy as np
import sys

# считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# # здесь продолжайте программу (используйте список lst_in)
# fl = 0
# for i in range(len(lst_in) - 1):
#     for j in range(len(lst_in[i]) - 1):
#         if lst_in[i][j] + lst_in[i+1][j+1] + lst_in[i+1][j] + lst_in[i][j+1] > 1:
#             fl += 1
# if fl:
#     print('НЕТ')
# else:
#     print('ДА')

# anothyer solution
# lst_in = [list(map(int, x.strip().split())) for x in s]
# flag = 'ДА'
# matrix = np.pad(lst_in, pad_width=1, mode='constant', constant_values=0)
# for x in range(1, 6):
#     for j in range(1, 6):
#         if matrix[j][x] == 1:
#              if matrix[j - 1][x - 1] == 1 or matrix[j][x - 1] == 1 or \
#              matrix[j - 1][x + 1] == 1 or matrix[j][x + 1] == 1 or \
#              matrix[j + 1][x + 1] == 1 or matrix[j + 1][x] == 1 or \
#              matrix[j + 1][x - 1] == 1 or matrix[j][x - 1] == 1:
#                 flag = 'НЕТ'
# print(flag)

# z = np.diag([2, 2, 2, 2, 2])
# print(z)
# fl = 'ДА'
# for i in range(len(z)):
#     for j in range(len(z)):
#         if z[0][0] != 2 or z[1][1] != 2 or z[2][2] != 2 or z[3][3] != 2 or z[4][4] != 2:
#             fl = 'НЕТ'
#             break
# else:
#     print(fl)
lst_in = [[2, 3, 4, 5, 6],
          [3, 2, 7, 8, 9],
          [4, 7, 2, 0, 4],
          [5, 8, 0, 2, 1],
          [6, 9, 4, 1, 2]]

fl = True
for i in range(len(lst_in)):
    for j in range( len(lst_in[i])):
        if lst_in[i][j] != lst_in[j][i]:
            fl = False
            break
if fl:
    print('ДА')
else:
    print('НЕТ')