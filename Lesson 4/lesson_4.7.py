x = float(input('vvedite ewe odno chislo')) 
a = float(input('vvedite chislo'))       
if x > 0:
    if a>=0:
        y=a*x
        print('y=',y)
    else:
        y=2*a*x
        print('y=',y)
else:
    y=2
    print('y=',y)