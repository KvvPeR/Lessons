class Human:
    def info(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Place Of Birth: {self.place_of_birth}, Year Of Birth: {self.year_of_birth}")
    def years(self, year):
        print(f"Year: {year - self.year_of_birth}")
    def __init__(self, name, surname, age, place_of_birth, year_of_birth):
        self.name = name
        self.surname = surname
        self.age = age
        self.place_of_birth = place_of_birth
        self.year_of_birth = year_of_birth
        
p1 = Human('Bebra', 'Bebrovna', 15, 'BEBRASTAN', 2006)
p2 = Human('Bebro4ka', 'Bebrovna', 17, 'BEBRASTAN', 2004)
#p1.name = "Den"
#p1.surname = "Dmitriev"
#p1.age = 24
#p1.place_of_birth = "UA"
#p1.year_of_birth = 1997

#p2 = Human()
#p2.name = "Ivan"
#p2.surname = "Tsurkan"
#p2.age = 15
#p2.place_of_birth = "UA"
#p2.year_of_birth = 2006

#p3 = Human()
#p3.name = "Bebra"
#p3.surname = ".lkgahuislg"
#p3.age = 2341
#p3.place_of_birth = "UA"
#p3.year_of_birth = 5643975

#p4 = Human()
#p4.name = "Kirill"
#p4.surname = "DIbill"
#p4.age = 15
#p4.place_of_birth = "UA"
#p4.year_of_birth = 2006

p1.info()
p2.info()
#p3.info()
#p4.info()
#p1.years(2021)
#p2.years(2021)
#p3.years(2021)
#p4.years(2021)