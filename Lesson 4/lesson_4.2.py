number1 = float(input('vvedite pervoe chislo'))
number2 = float(input('vvedite vtoroe chislo'))
if number1 > number2:
    number1 = 1
    number2 = 0
    print(number1, number2)
elif number2 > number1:
    number1 = 0
    number2 = 1
    print(number1, number2)
else:
    print('oni ravni')