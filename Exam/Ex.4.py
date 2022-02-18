users=['user_1', 'user_2', 'user_3', 'user_4']
ver_users=[]

print(f'Неверефицированые пользователи: {users}')
print(f'Верефецированые пользователи: {ver_users}')
print(f'\t\t\tПроверяем пользователя...')
while users:
    ver=users.pop(0)
    ver_users.append(ver)
print(f'Неверефицированые пользователи: {users}')
print(f'Верефецированые пользователи: {ver_users}')