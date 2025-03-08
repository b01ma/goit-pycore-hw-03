
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

# Вимоги до завдання:
# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.


# Рекомендації для виконання:
# Імпортуйте модуль datetime.
# Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
# Отримайте поточну дату, використовуючи datetime.today().
# Розрахуйте різницю між поточною датою та заданою датою.
# Поверніть різницю у днях як ціле число.

import datetime as dt
from datetime import datetime as dtdt

def get_days_from_today(date):
    now = dtdt.now()
    print(now)
    
get_days_from_today('2024-04-11')