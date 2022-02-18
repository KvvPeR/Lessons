lst = [4,16,64,256]
list_1 = [i**0.5 for i in lst]
def gen():
    for i in list_1:
        yield i
y = gen()
g = 0
while g<len(list_1):
    print(next(y))
    g+=0
