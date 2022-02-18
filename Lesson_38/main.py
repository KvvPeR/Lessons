import sqlite3

bd = sqlite3.connect('user.db')
sql = bd.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS user(
    login TEXT,
    password TEXT,
    cash INT
)''')
bd.commit()
login_user = input('Login: ')
password_user = input('Password: ')
cash_user = input('Your cash: ')
sql.execute(f"SELECT login FROM user WHERE login = '{login_user}'")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO user VALUES (?,?,?)",(login_user, password_user, 0))
    bd.commit()
    print('Вы зарегестрированы!')
else:
    print('Такая учетная запись уже сущевствует!')
    for i in sql.execute("SELECT * FROM user"):
        print(i)