dct = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
    }
dct_s={k:['even' if v%2==0 else 'odd'] for k, v in dct.items()}
print(dct_s)