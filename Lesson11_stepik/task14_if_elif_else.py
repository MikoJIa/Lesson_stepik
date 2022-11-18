# this is an awesome text необходимо найти самое длинное слово в предложении!!
txt = input().split()
max = len(txt[0])
print(max)
l = []
for i in range(len(txt)):
    if len(txt[i]) > max:
        max = len(txt[i])
        l.append(txt[i])
print(*l)

txt = list(input().split())
print(max(txt,key=len))