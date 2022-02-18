class Circle:
    PI = 3.14
    c_v = 0
    def __init__(self, radius):
        self.radius = radius
        Circle.c_v += 1
    def lenth(self):
        print(f"{2*self.PI*self.radius}")
    
    def square(self):
        print(f"{Circle.PI*self.radius**2}")
n = int(input('Vvedite 4islo'))
m = int(input('Vvedite 4islo'))
c1 = Circle(n)
c1.lenth()
c1.square()
p = Circle.c_v
print(p)
c2 = Circle(m)
c2.lenth()
c2.square()

print(Circle.c_v)