#Площадь треугольника по формуле Герона
import math
a=int(input('Первая сторона'))
b=int(input('Вторая сторона'))
c=int(input('Третья сторона'))
p=(a+b+c)/2
d= math.sqrt(p*(p-a)*(p-b)*(p-c))
print('Площадь' , d)
