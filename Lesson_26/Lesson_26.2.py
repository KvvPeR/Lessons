class Human:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
    def hello(self):
        print(f'Hello {self.name} {self.surname}. Age: {self.age}')
class Student(Human):
    def study(self):
        print(f'{self.name} studies')
class Teacher(Human):
    def teach(self):
        print(f'{self.name} teaches web-development')

n=input('Введите своё имя: ')
s_n=input('Введите свою фамилию: ')
a=int(input('Введите свой возраст: '))

s_1=Student(n, s_n, a)
s_1.hello()
s_1.study()

n_1=input('Введите имя учителя: ')
s_n_1=input('Введите фамилию учитиеля: ')
a_1=int(input('Введите возраст учителя: '))
t_1=Teacher(n_1, s_n_1, a_1)
t_1.hello()
t_1.teach()