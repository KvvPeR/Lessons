dct={
    'a':2,
    'b':4,
    'c':8,
    'd':10
    }

dct_g={i:j for i, j in dct.items() if j>2}
print(dct_g)