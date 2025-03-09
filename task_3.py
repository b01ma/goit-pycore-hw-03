'''
    У вашій компанії ведеться активна маркетингова кампанія за допомогою SMS-розсилок. Для цього ви збираєте 
    телефонні номери клієнтів із бази даних, але часто стикаєтеся з тим, що номери записані у різних форматах. 

    Ваш сервіс розсилок може ефективно відправляти повідомлення лише тоді, коли номери телефонів представлені у коректному форматі. 
    Тому вам необхідна функція, яка автоматично нормалізує номери телефонів до потрібного формату, видаляючи всі зайві символи та 
    додаючи міжнародний код країни, якщо потрібно.

    Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи 
    тільки цифри та символ '+' на початку. Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі 
    та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. Якщо номер не містить міжнародного коду, 
    функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть придатними для відправлення SMS.
'''


import re

def normalize_phone(phone_number: str) -> str:
    
    '''
        Function receives a phone number and transforms into the valid format
        
        :params phone_number: string with phone number in any format
        :return: string with phone number in format '+380XXXXXXXXX'
    '''
    #Solution #1
    striped_phone = re.sub(r'[^\d+]', '', phone_number).strip()
    final_phone_number = ''
    
    if striped_phone.startswith('+38'):
        final_phone_number = striped_phone
    elif (len(striped_phone) == 12): 
        final_phone_number = f'+{striped_phone}'
    elif (len(striped_phone) == 10):
        final_phone_number = f'+38{striped_phone}'
    elif (len(striped_phone) == 9):
        final_phone_number = f'+380{striped_phone}'
    else:
        print('Phone number is not valid')
        return ''
    
    # Solution #2
    # trimmed_phone_number =  re.sub(r'\D', '', phone_number)
    # phone_number_no_country_code = trimmed_phone_number[-9:]
    # country_code = '+380'
    
    # final_phone_number = country_code + phone_number_no_country_code
    
    return final_phone_number
