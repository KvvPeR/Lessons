class Rectangle:
    def __init__(self, a, b):
        self.a = 2
        self.b = 3
    def ab(self,a,b):
        s = self.a*self.b
        print(s)
my_ab = Rectangle(2,3)
my_ab.ab(2,3)



#class Rectangle:
#    def __init__(self, a, b):
#        self.a = m
#        self.b = n
#    def ab(self,a,b):
#        s = self.a*self.b
#        print(s)
#m = int(input('Введите высоту прямоугольника'))
#n = int(input('Введите длинну прямоугольника'))
#my_ab = Rectangle(m,n)
#my_ab.ab(m,n)