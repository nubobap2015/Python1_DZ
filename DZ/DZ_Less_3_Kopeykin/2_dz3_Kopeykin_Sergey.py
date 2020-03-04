# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def f_print_user_data(fname, lname, bornyear, town, email, phone):
    """
    Вывод данных о пользователе одной строкой
    :param fname: Имя
    :param lname: Фамилия
    :param bornyear: Год рождения
    :param town: город проживания
    :param email: почта
    :param phone: телефон
    """
    print(f' Имя: {fname}\n Фамилия: {lname}\n Год рождения: {bornyear}\n Город проживания: {town}'
          f'\n Email: {email}\n Телефон{phone}')


f_print_user_data(fname='Иван', lname='Петров', email='ivan2000@zlo.ru', bornyear='2000',
                town='Рига', phone='+7(954)223-45-21')

