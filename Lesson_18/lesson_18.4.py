import random
n=int(input('Первое число'))
m=int(input('Второе число'))
matrix = [[random.randint(0,9) for w in range(m)] for q in range(n)]
print('Matrix =====>')
for i in matrix:
    print(f"\t\t{i}")
diagonal = [matrix[w][q] for q in range(n) for w in range(m) if q==w]
print(diagonal)
