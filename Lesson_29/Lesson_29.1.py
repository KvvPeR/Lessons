class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
        self.adometr = 0
    def get_discript_name(self):
        a = f"Марка машины {self.mark}, модель машины {self.model}, год выпуска машины {self.year}"
        print(a)
    def read_adometr(self):
        b = f"Пробег вашей машины равен {self.adometr} киллометрам"
        print(b)
    def update_adometr(self, n):
       #self.adometr = n
        if n>=self.adometr:
            self.adometr = n
        else:
            print('Пробег скинуть невозможно')
    def incriment_adometr(self, m):
        self.adometr += m
class ElectroCar(Car):
    def __init__(self, mark, model, year, battary):
        super().__init__(mark, model, year)
        self.battary = battary
        print(f'Марка машины {self.mark}, модель машины {self.model}, год выпуска машины {self.year}, с батареей {self.battary}')
    def your_battary(self, mark, model, year, z, money):
        if money >= 1000000:
            print('Теперь это ваша машина: марки {mark}, модели {model}, {year} года выпуска имеет батарею с вместимостью {z} милиампер. Её стоимость {money}')
        else:
            print('idi gulyai')
my_new_car = Car('Tesla', 'Model X', 2022)
n = int(input('Введите пробег вашей машины: '))
m = int(input('Добавьте пробег вашей машине: '))
z = int(input('Размер вашей батареи'))
money = int(input('Введите цену данной машины: '))
my_new_car.adometr = 123
my_new_car.update_adometr(n)
my_new_car.incriment_adometr(m)
my_new_car.read_adometr()
my_new_car.get_discript_name()
my_new_car1 = ElectroCar('Tesla', 'Model X', 2022, f'{z} Милиампер')
my_new_car1.your_battary('Tesla', 'Model X', 2022, z, money)
