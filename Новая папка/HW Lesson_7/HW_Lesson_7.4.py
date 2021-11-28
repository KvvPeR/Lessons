dop_pizza = str(input('Введите дополнение к пицце'))
a = 'quit'
while dop_pizza:
    if dop_pizza == a:
        break
    else:
        b = str(input('Введите дополнение к пицце'))
        if b == a:
            break
        print(f"Дополнение {b} было включено в заказ")
        