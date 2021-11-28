import random
numbers = [random.randint(1,1000000) for i in range(1,30)]
print(numbers)
for n in numbers:
    if n%2==0:
        print(n)
    else:
        print('kirill lox')
        