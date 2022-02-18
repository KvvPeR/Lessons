sum = int(input('Summa: '))
p= int(input('Percent: '))
for i in range(5):
    i =i+1
    sum = sum + sum*(p/100)
    print(int(sum))