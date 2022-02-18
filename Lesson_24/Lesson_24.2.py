class Human:
    def info(self,n):
        for i in range(n):
            print(f'\tHuman_1:\nИмя: {self.name}\nФамилия: {self.surname}\nМесто рождение: {self.place_of_birth} ')

n=int(input('Введите количество выводов для первого человека: '))
n_1=int(input('Введите количество выводов для второго человека: '))
p_1=Human()
p_1.name='Ivan'
p_1.surname='Tsurkan'
p_1.place_of_birth='Ukraine'

p_2=Human()
p_2.name='Kirill'
p_2.surname='Tubik'
p_2.place_of_birth='Ukraine'

p_1.info(n)
p_2.info(n_1)
#print(f'Human_1:\nИмя: {p_1.name}\nФамилия: {p_1.surname}\nМесто рождение: {p_1.place_of_birth} ')
#print(f'Human_2:\nИмя: {p_2.name}\nФамилия: {p_2.surname}\nМесто рождение: {p_2.place_of_birth} ')