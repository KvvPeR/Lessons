n=int(input('Введите степень в которую хотите возвести: '))
key=["a", "d", "c"]
value=[1, 2, 3]
dct={k:v**n for k, v in  zip(key, value)}
print(dct)