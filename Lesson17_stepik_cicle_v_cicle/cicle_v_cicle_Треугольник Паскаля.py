n = 7
t_p = []
for i in range(1, n + 1):
    t_p.append([1] * i)
for i in range(len(t_p)):
    for j in range(0, i - 1):
        t_p[i][j + 1] = t_p[i - 1][j] + t_p[i - 1][j + 1]
for r in t_p:
    print(r)
# enother solution
N = 8
t = []

for i in range(N):
    row = [1] * (i+1)
    print(row)
    for j in range(0, i + 1):
        if j != 0 and j != i:
            row[j] = t[i - 1][j - 1] + t[i - 1][j]
    t.append(row)
for x in t:
    print(x)
