class Python:
    def __init__(self, a):
        self.a = a
    def construktor(self, a):
        q = a.swapcase()
        print(q)
a = input("Введите слово для перевода его в верхний регистр!")
my_word = Python(a)
my_word.construktor(a)