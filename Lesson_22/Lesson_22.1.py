list_my = ['a','b','c','d','e','f']
def gen():
    for i in list_my:
        yield i
y = gen()
print(next(y))
print(next(y))