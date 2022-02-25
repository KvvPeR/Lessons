import math
x = int(input('Введите значение х: '))
y = int(input('Введите значение y: '))
if x == abs(x) and y == abs(y):
    print("Ваша точка в ПЕРВОЙ четверти")
elif x != abs(x) and y == abs(y):
    print("Ваша точка в ВТОРОЙ четверти")
elif x != abs(x) and y != abs(y):
    print("Ваша точка в ТРЕТЬЕЙ четверти")
elif x == abs(x) and y != abs(y):
    print("Ваша точка в ЧЕТВЕРТОЙ четверти")