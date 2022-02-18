def gen():
    i=1
    while True:
        if i>1:
            for g in range(2,i):
                if i%g==0:
                    break
                else:
                    yield i
        i+=1
for a in gen():
    print(a)

