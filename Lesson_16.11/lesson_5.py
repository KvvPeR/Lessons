import random
n=int(input('1'))
m=int(input('2'))
matrica = [[random.randint(0,9) for w in range(m)] for q in range(n)]
print('Matrix ==>')
for f in matrica:
    print(f"\t {f}")
diagonal = [matrica[q][w] for q in range(n) for w in range(m) if q == w]
print(f"Glavnaya diagonal ==> {diagonal}")
vtrstroka = [matrica[q][w] for q in range(n) for w in range(m) if q == 1]
print(f"Vtrstroka ==> {vtrstroka}")
thirdstolbec = [matrica[q][w] for q in range(n) for w in range(m) if w == 2]
print(f"Thirdstolbec ==> {thirdstolbec}")