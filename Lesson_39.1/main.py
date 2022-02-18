import sqlite3
from random import randint

bd = sqlite3.connect("user.db")
sql = bd.cursor() #взаимодействие с таблицей
sql.execute('''CREATE TABLE IF NOT EXISTS user(
    login TEXT,
    password TEXT,
    cash INT
)''' )
bd.commit()
def Reg():
    user_login = input('Login:')
    user_password = input('Password:')
    user_cash = input('Cash: ')
    sql.execute(f"SELECT login FROM user WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user VALUES(?, ?, ?)", (user_login, user_password, 0))
        bd.commit()
        print('Зарегестрировано')
    else:
        print('Такая учетная запись существует')
    for i in sql.execute("SELECT * FROM user"):
        print(i)
#Reg()
def casino():
    user_log = input('Введите ваш Login: ')
    number = randint(1,4)
    rand_att = int(input('Введите число от 1 до 4'))
    sql.execute(f"SELECT login FROM user WHERE login = '{user_log}'")
    if sql.fetchone() is None:
        print('Такой пользователь не зарегестрирован!')
        Reg()
    else:
        if number == rand_att:
            sql.execute(f"UPDATE user SET cash = {1000} WHERE login = '{user_log}'")
            bd.commit()
            print('Вы выиграли!')
            for i in sql.execute("SELECT * FROM user"):
                print(i)
        else:
            print('Вы проиграли(')
            for i in sql.execute("SELECT * FROM user"):
                print(i)
casino()