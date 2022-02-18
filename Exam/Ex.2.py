import random
import math
n = int(input('Kol-vo chisel'))
q = [random.randint(0,16) for w in range(n)]
print(q)
p = 1
for w in q:
    p *= w
print(w)