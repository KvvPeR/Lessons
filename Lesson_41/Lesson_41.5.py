import math
x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
if x > y:
    v = x+y
    z = math.sqrt(v)
    print(z)
elif x <= y:
    v = x+y
    z = math.log(v)
    print(z)