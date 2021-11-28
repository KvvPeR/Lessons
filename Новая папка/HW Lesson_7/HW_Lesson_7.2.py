table = int(input('Кол-во мест'))
if table>8:
    print('Вам нужно немного подождать')
elif 0<table<9:
    print('Ваш стол готов')
elif table<1:
    print('Такого не может быть!')