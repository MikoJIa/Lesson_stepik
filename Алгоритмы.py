import graphics as gr

def build_house():
    '''функция, которая рисует дом'''
    pass


window = gr.GraphWin('Russion game', 100, 100)
build_house()

print('Ура дом построен')


a = [0] * 10
n = 0
x = int(input())
while n < len(a):
    for i in range(1, x+1):
        a[n] = i
        n += 1
print(a)
