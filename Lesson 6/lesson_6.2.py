n = int(input('Vvedite chislo'))
print(n)
s=0.5
p=0
for n in range(1,n+2):
    
    p += s
    s /= 2
    print(n,float(p))
    
print(n,float(p))