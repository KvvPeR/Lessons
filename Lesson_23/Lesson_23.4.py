a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))

s=lambda a,b:a+b
s_0=lambda a,b:a-b
s_1=lambda a,b:a*b
s_2=lambda a,b:a/b

print(f'Сумма: {s(a,b)}')
print(f'Разница: {s_0(a,b)}')
print(f'Произведение: {s_1(a,b)}')
print(f'Деление: {s_2(a,b)}')