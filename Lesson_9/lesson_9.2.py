def pizza(size,*nazvanie):
    
    print(f"Вы выбрали такие пиццы, с размером {size.title()}:")
    for i in nazvanie:
        print(f"- {i.title()}")
        
#  Основная программа!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
razmer = str(input('Введите размер пиццы:'))
pizza(razmer, 'gavai')
pizza(razmer, 'peperonni', '4sira', 'myasnaya')