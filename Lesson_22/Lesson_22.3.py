#числа Фибоначчи
def gen(n):
    a,b = 1,1
    for i in range(n):
        yield a
        a,b = b,a+b
n = int(input('Введите количество чисел'))
y = list(gen(n))
print(y)