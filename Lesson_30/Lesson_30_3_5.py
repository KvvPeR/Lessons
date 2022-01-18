class Shop:
    def __init__(self, shop_name, store_type, units, number, x):
        self.shop_name = shop_name
        self.store_type = store_type
        self.units = units
        self.number = number
        self.x = x
    def describe_shop(self, shop_name, store_type):
        a = shop_name
        b = store_type
        print(f"{self.store_type.title()} магазин под названием {self.shop_name.title()} уже открыт!")
    def number_of_units(self, units):
        print(f"На данный момент в магазине товар в количестве ==> {self.units}")
    def set_number_of_units(self, number):
        print(f"На данный момент в магазине такое кол-во видов товаров ==> {self.number}")
    def increment_number_of_units(self, x):
        self.x = self.units + x
        print(f"Теперь в магазине такое кол-во товаров ==> {self.x}")
class Discount(Shop):
    def __init__(self, shop_name, store_type, units, number, x, items):
        self.shop_name = shop_name
        self.store_type = store_type
        self.units = units
        self.number = number
        self.x = x
        self.items = items
    def get_discounts_products(self, items):
        print(f"Список ассортемента на который действует скидка: {self.items}")
        
m = input("Введите название вашего магазина: ")
n = input("Введите тип вашего магазина: ")
k = int(input("Введите количество товара в магазине на данный момент: "))
q = int(input("Введите количество видов товара в магазине: "))
w = int(input("Во сколько раз вы бы хотели увеличить кол-во товаров в магазине?: "))
z = input("Введите список продуктов на которые действует скидка: ")
store = Shop(n,m,k,q,w)
store.describe_shop(n,m)
store.number_of_units(k)
store.set_number_of_units(q)
store.increment_number_of_units(w)
store = Discount(n,m,k,q,w,z)
store.get_discounts_products(z)
