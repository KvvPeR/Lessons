class User:
    def __init__(self, first_name, last_name, age, nickname, login_attemps):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nickname = nickname
        self.login_attemps = 0
    def describe_user(self, first_name, last_name):
        print(f"Ваше имя: {first_name.title()} {last_name.title()}")
    def greeting_user(self, first_name, last_name):
        print(f"Доброго времени суток {first_name.title()} {last_name.title()}")
    def increment_login_attemps(self, login_attemps):
        
    def reset_login_attemps(self, login_attemps):
        self.login_attemps = 0
        print(self.login_attemps)
first_name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")
nickname = input("Введите ваш никнейм: ")
login_attemps = input("Введите данные для входа: ")
user = User(first_name, last_name, age, nickname)
user.describe_user(first_name, last_name)
user.greeting_user(first_name, last_name)