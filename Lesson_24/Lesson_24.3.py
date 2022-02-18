class Human:
    def rez_age(self, m):
        return m-self.year


year=int(input('Введите год, на сегодняшний момент: '))
p_1=Human()
p_1.name='Ivan'
p_1.surname='Tsurkan'
p_1.place_of_birth='Ukraine'
p_1.year=2006

p_2=Human()
p_2.name='Kirill'
p_2.surname='Bezdar'
p_2.place_of_birth='Ukraine'
p_2.year=2005

print(f'Возраст первого человека: {p_1.rez_age(year)}')
print(f'Возраст второго человека: {p_2.rez_age(year)}')