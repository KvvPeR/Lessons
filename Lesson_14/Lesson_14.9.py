import random
numbers=[ random.randint(1,1000) for item in range(16)]
print(numbers)

for i in numbers:
    if i%2==0:
        print(f'\n{i}')