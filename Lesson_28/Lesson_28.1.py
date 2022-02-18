class Human:
    def __init__(self, name,  surname, year_of_birth, place_of_birth):
        self.name=name
        self.surname=surname
        self.year_of_birth=year_of_birth
        self.place_of_birth=place_of_birth
    def info(self):
        print(f"Name: {self.name} \nSurname: {self.surname} \nYear of birth: {self.year_of_birth} \nPlace of birth: {self.place_of_birth}")
    def age(self, years):
        return years-self.year_of_birth

name= input('Введите своё имя: ')
surname=input('Ввелите свою фамилию: ')
year_of_birth=int(input('Введите год рождение: '))
place_of_birth=input('Введите место рождения: ')
years=int(input('Введите текущий год: '))
p_1=Human(name, surname, year_of_birth, place_of_birth)
p_1.info()
print(p_1.age(years))

name_2= input('Введите своё имя: ')
surname_2=input('Ввелите свою фамилию: ')
year_of_birth_2=int(input('Введите год рождение: '))
place_of_birth_2=input('Введите место рождения: ')
years_2=int(input('Введите текущий год: '))
p_2=Human(name_2, surname_2, year_of_birth_2, place_of_birth_2)
p_2.info()
print(p_2.age(years_2))