def gen():
    yield
    print('первый перебор')
    yield
    print('второй перебор')
y = gen()
print(next(y))
print(next(y))
print(next(y))

