'''
    У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати 
    цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег 
    потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

    У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його 
    день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати 
    це та переносити дату привітання на наступний робочий день, якщо необхідно.
'''
import datetime as dt
from datetime import datetime as dtdt

def get_upcoming_birthdays(users: list) -> list:
    '''
        Function returns a list of users who have a birthday in the next 7 days
        :param users: List of dictionaries with user name and birthday
        :return: List of dictionaries with user name and congratulation date
    '''
    result = []
    if not users:
        return result
    
    today = dtdt.today().date()
    current_year = today.year
    
    days_to_monday = (7 - today.weekday()) % 7 
    next_monday = today + dt.timedelta(days=days_to_monday)
    next_friday = next_monday + dt.timedelta(days=4)
    days_to_next_friday = next_friday - today
    
    for user in users:

        try:
            name = user['name']
            birthday_str = user['birthday']
            if not birthday_str or not name:
                continue
            birthday_obj = dtdt.strptime(birthday_str, "%Y.%m.%d").date()
        except ValueError as e:
            print(f'Invalid date format for user {name}: {e}')
            continue
        
        birthday_this_year = dtdt(current_year, birthday_obj.month, birthday_obj.day).date()

        if birthday_this_year < today:
            birthday_this_year = dtdt(current_year + 1, birthday_obj.month, birthday_obj.day).date()
        
        days_to_birthday = birthday_this_year - today
        day_of_birthday = birthday_this_year.weekday()
        
        if days_to_birthday < days_to_next_friday:
            congratulation_date = birthday_this_year
            if day_of_birthday == 5 or day_of_birthday == 6:
                congratulation_date = next_monday
            
            result.append({'name': name, 'congratulation_date': congratulation_date.strftime("%Y.%m.%d")})

    return result
    