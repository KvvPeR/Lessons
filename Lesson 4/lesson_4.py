money = int(input('Vvedite kol-vo'))
percent = int(input('Vvedite %'))
year=int(input('Введите кол-во месяцов'))
if 24>year>11:
    Sum = money + money*percent/100
    print(Sum)
elif 36>year>23:
    Sum = money + money*percent/100
    Sum1 = Sum + Sum*percent/100
    print(Sum1)
elif 48>year>35:
    Sum = money + money*percent/100
    Sum1 = Sum + Sum*percent/100
    Sum2 = Sum1 + Sum1*percent/100
    print(Sum2)
elif 60>year>47:
    Sum = money + money*percent/100
    Sum1 = Sum + Sum*percent/100
    Sum2 = Sum1 + Sum1*percent/100
    Sum3 = Sum2 + Sum2*percent/100
    print(Sum3)
elif 72>year>59:
    Sum = money + money*percent/100
    Sum1 = Sum + Sum*percent/100
    Sum2 = Sum1 + Sum1*percent/100
    Sum3 = Sum2 + Sum2*percent/100
    Sum4 = Sum3 + Sum3*percent/100
    print(Sum4)
elif 84>year>71:
    Sum = money + money*percent/100
    Sum1 = Sum + Sum*percent/100
    Sum2 = Sum1 + Sum1*percent/100
    Sum3 = Sum2 + Sum2*percent/100
    Sum4 = Sum3 + Sum3*percent/100
    Sum5 = Sum4 + Sum4*percent/100
    print(Sum5)
else:
    my_money = 5000
    print(my_money)