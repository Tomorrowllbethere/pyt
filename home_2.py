import random

def get_numbers_ticket(min, max, quantity):
        # створення логічного виразу умови  
    if (min >=1 and min<1000) and (max<1000 and max!=1) and (quantity<=max and quantity>0):
        numbs= list(range(min,max+1))# створення списку з заданим діапазоном
        numbers=random.sample(numbs, quantity) # створення списка з рандомними унікальними числами в діапазоні
        lottery_numbers = sorted(numbers)# відсортованний список
    return lottery_numbers
    
try:                # перевірка на коректний ввід чисел
    min=int(input('Введи мінімальне число для пошуку\n'))
    max=int(input('Введи максимальне число для пошуку\n'))
    quantity=int(input('Введи бажану кількість чисел\n'))
except ValueError:
    print('Здається, це не було число.\n Спробуй ще раз')

lottery_numbers = get_numbers_ticket(min,max,quantity) # виклик функції
print("Ваші лотерейні числа: ", lottery_numbers)
