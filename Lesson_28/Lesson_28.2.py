class Human:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print(f"Person created!")
    def info(self):
        print(f"Name: {self.name} \nAge: {self.age}")
    def hello(self):
        print(f"{self.name} says hello!")
class Student(Human):
    def study(self):
        print(f"Name student: {self.name} - studing")
    def hello(self):
        print(f"Student created, {self.name} is {self.age}")
class Teacher(Human):
    def teach(self):
        print(f"Name teacher: {self.name} - teahing")

name=input('Введите имя: ')
age=int(input('Введите возраст: '))
s_1=Student(name, age)
s_1.info()
s_1.study()
s_1.hello()

name=input('Введите имя: ')
age=int(input('Введите возраст: '))
t_1=Teacher(name, age)
t_1.info()
t_1.teach()