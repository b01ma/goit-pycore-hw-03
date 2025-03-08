'''
    Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і 
    в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

    Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для 
    таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

'''

import random

def get_number_ticket(min: int, max: int, quantity:int) -> list[int]:
    '''
        Function generate unique random numbers from the given range 
        
        :params min: Minium number, must be >= 1
        :params max: Maximum number, must be <= 1000
        :params quantity: Number of unique numbers to generate
        "return: A sorted list of unique random numbers
    '''
    
    if min < 1 or min > max:
        print(f'Minimum number has to be greater then 0 and not greater then Maximum - {max}')
        return []
    if max > 1000 or max < min:
        print(f'Maximum number has to be less than 1000 and grater then Minimum number - {min} ')
        return []
    if quantity > (max-min + 1):
        print (f'Quantity has to be less then difference between Maximum and Minimum number {max-min+1}')
        return []
    
    # Solutions #1
    numbers = set()
    
    while len(numbers) < quantity:
        int = random.randint(min, max)
        numbers.add(int)
    
    numbers_list = list(numbers)
    numbers_list.sort()
    
    # Solution #2
    # numbers = list(range(min, max+1))
    # numbers_list = random.sample(numbers, quantity)
    
    return numbers_list
    