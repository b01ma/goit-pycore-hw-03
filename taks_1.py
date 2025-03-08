
'''
    Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

    Вимоги до завдання:
    Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
    Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
    У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
    Для роботи з датами слід використовувати модуль datetime Python.
'''

import datetime as dt
from datetime import datetime as dtdt

def get_days_from_today(date: str) -> int:
    '''
        Function calculates the number of days between current date and provided date
        
        :param date: String in 'yyyy-mm-dd' format
        :return: Integer with number of days  between current date and provided date
            Returns -1 if there's an error (e.g., invalid date format).
    '''
    
    date_format = "%Y-%m-%d"
    
    try: 
        f_date = dtdt.strptime(date, date_format)
    except ValueError:
        print('Format of the date is not correct. The format should be "yyyy-mm-dd"')
        return -1
    
    current_date = dtdt.today()
    
    diff = current_date - f_date

    return diff.days
