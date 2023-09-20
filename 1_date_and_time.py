"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import timedelta, datetime

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = datetime.now()
    delta_1 = timedelta(days=1)
    delta_30 =timedelta(days=30)
    

    print(dt_now.strftime('%Y.%m.%d'))
    print((dt_now - delta_1).strftime('%Y.%m.%d'))
    print((dt_now - delta_30).strftime('%Y.%m.%d'))


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print(type(date_dt))
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
