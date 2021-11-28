def describe_pet(pet_name, animal_type="собака"):
#Выводит информацию о животном
   print(f"\nУ меня есть {animal_type}.")
   print(f"Мой {animal_type} и его зовут {pet_name.title()}.")
 
describe_pet(pet_name="вилли")