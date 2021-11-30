name_user={
    'Ivan':15,
    'Kirill':49,
    'Renat':14,
    'Den':24,
    'Nella':18
    }
user_auto={
    'Jigul':1990,
    'Ferrari':2021,
    'BMW':2020
    }
data_user=name_user|user_auto
print(data_user)
name_user|=user_auto
print(name_user)
c=name_user.keys()
print(c)
for i in c:
    print(i)
value=name_user.values()
for v in value:
    print(v)
for a, s in name_user.items():
    print(f'{a} ---> {s}')
abc=name_user.get('Vlad', 'User not founded')
print(abc)
name_user.clear()
print(name_user, 'Game over')