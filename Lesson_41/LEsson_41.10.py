x = int(input('Введите значение х: '))
if x > 0:
    y = 2*x-10
    print(y)
elif x == 0:
    y = 0
    print(y)
else:
    y = 2*abs(x)- 1
    print(y)