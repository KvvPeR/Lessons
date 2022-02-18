#a = [1,1,2,3,5,8,13,21,34,55,89]
#b = [i for i in a if i<5]
#print(b)
#
#import random
#import math
#n = int(input('Kol-vo chisel'))
#q = [random.randint(0,16) for w in range(n)]
#print(q)
#p = 1
#for w in q:
#    p *= w
#print(w)
#
#import math
#lst = [11,5,8,32,15,3,20,132,21,4,555,9,20]
#z=0
#for i in lst:
#    if i%3==0 and i<30:
#       print(i)
#    else:
#        z+=i
#print(z)
#
diction = {'a' : 2, 'b' : 4, 'c' : 6 , 'd' : 8}
#for i in diction.values():
#    if i>2:
#        print(i)
#
#a = [1,2,3,4,5,6]
#b = ['a','b','c','d','e','f']
#
import random
n = int(input('Vvedite kol-vo strochek'))
m = int(input('Vvedite kol-vo stolbikov'))
matrix = [[random.randint(0,9) for w in range(m)] for q in range(n)]
for a in matrix:
        print(a)
diagonal = [matrix[w][q] for w in range(n) for q in range(m) if w==q]
print('Главная диагональ ===>',diagonal)
k = int(input('Номер строки'))
p = int(input('Номер столбца'))
item = [matrix[k-1][w] for w in range(m)]
item1 = [matrix[q][p-1] for q in range(n)]
print(item)
print(item1)
r = int(input('Номер строки элемента'))
t = int(input('Номер столбца элемента'))
item2 = matrix[r-1][t-1]
print(item2)