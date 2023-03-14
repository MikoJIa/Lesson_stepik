import mymodul
def magick_func(a: int, b: int) -> int:
    if a > b:
        return a - b
    return b - a


print(magick_func(1, 3))

d = dict()
d[1] = 'one'
d[2] = 'two'
d[3] = 'free'
d['pi'] = 3.14
print(d)
print(d['pi'])


class Vector:
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except ValueError:
            self.x = 0.0
            self.y = 0.0

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return Vector(newx, newy)

    def __str__(self):
        return '(%f, %f)' %(self.x, self.y)


u = Vector(3, 4)
v = Vector(3, 6)


print(u.norm())  # 5.0
print(Vector(5, 12).norm())  # 13.0
print(u + v)  # (6.000000, 10.000000)