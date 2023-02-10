def say_name(name):
    def say_goodbye():
        print("Don't say me goodbye, " + name + "!")

    return say_goodbye()


f = say_name("Sergey")
f2 = say_name("Python")

#

def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start
    return step

c1 = counter(10)
c2 = counter()
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())

# Предположим, что мы хотим создать функцию, которая, удаляла бы ненужные символы в конце и в начале строки

def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)
    return do_strip


strip1 = strip_string()
strip2 = strip_string(" !?,.;")

print(strip1(' Hello Python!.. '))
print(strip2(' Hello Python!.. '))