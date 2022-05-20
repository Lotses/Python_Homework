import datetime


class TerminateProg(Exception):
    pass





# #_____________________ Задание 1 (Запрашивать два числа, поделить, проверить знаменатель на ноль)
# print('Задание №1 ↓')
#
#
# def division():
#     """
#     Запрашивает два числа и делит одно число на другое
#
#     () -> input(number), input(number) -> number
#     >>> division() -> 10, 2
#     5
#     """
#
#     try:
#         num1 = input('Введите числитель : ')
#         if num1 == '%':
#             raise TerminateProg
#         num2 = input('Введите знаменатель : ')
#         if num2 == '%':
#             raise TerminateProg
#         return f' Результат деления: {round(float(num1) / float(num2), 2)}'
#     except TerminateProg:
#         return "Введён символ %, программа завершает работу."
#     except ZeroDivisionError:
#         print('На ноль делить нельзя! Давайте попробуем ещё раз (или введите "%" для завершения):')
#         return division()
#     except ValueError:
#         print('Необходимо ввести число! Давайте попробуем ещё раз (или введите "%" для завершения):')
#         return division()
#
#
# print(division(), end='\n' * 2)
#
# # _____________________ Задание 2 (Собрать данные о пользователя через именнованные аргументы и вывести одной строкой)
# print('Задание №2 ↓')
#
#
# def birthday():
#     """ Забирает от пользователя год, месяц и день рождения, проверяет на корректность данных """
#
#     def date_year():
#         """ Получает и обрабатывает год рождения """
#         try:
#             year = int(input('Введите год рождения в формате уууу : '))
#             if len(str(year)) < 4:
#                 print('Пожалуйста, введите год в формате уууу')
#                 return date_year()
#             if (datetime.datetime.now().year - year) > 122:
#                 print(f'Вряд ли пользователю {datetime.datetime.now().year - year} лет, попробуйте ещё раз')
#                 return date_year()
#             elif datetime.datetime.now().year < year:
#                 print('Человек ещё не родился, попробуйте ещё раз')
#                 return date_year()
#             return year
#         except ValueError:
#             print('Необходимо ввести число, давайте попробуем ещё раз')
#             return date_year()
#
#     def date_month():
#         """ Получает и обрабатывает месяц рождения """
#         month_ru = {'январь': '01', 'февраль': '02', 'март': '03', 'апрель': '04', 'май': '05', 'июнь': '06',
#                     'июль': '07', 'август': '08', 'сентябрь': '09', 'октябрь': '10', 'ноябрь': '11', 'декабрь': '12',
#                     }
#         month = input('Введите месяц рождения : ').lower()
#         if month.isalpha():
#             if month in month_ru:
#                 return month_ru[month]
#             else:
#                 print('Такого месяца не существует, попробуйте ещё раз')
#                 return date_month()
#         elif month.isnumeric():
#             if (int(month) > 12) or (int(month) < 1):
#                 print('Такого месяца не существует, попробуйте ещё раз')
#                 return date_month()
#             else:
#                 return month
#         else:
#             print('Введён неверный формат месяца : ')
#             return date_month()
#
#     def date_day():
#         """ Получает и обрабатывает день рождения """
#         day = int(input('Введите день рождения в формате дд : '))
#         try:
#             if (day > 31) or ((int(d_m) == 2) and (day > 29)) or (day < 1):
#                 print('Такого числа нет в месяце, попробуйте ещё раз')
#                 return date_day()
#             return day
#         except ValueError:
#             print('Пожалуйста, введите цифры дня в формате дд :')
#             return date_day()
#
#     d_m = date_month()
#     return f'{date_day()}.{d_m}.{date_year()}'
#
#
# def user_email():
#     """ Запрашивает и проверяет на корректность """
#     email = input('Введите адрес электронной почты : ')
#     if not '@' in email:
#         print('Адрес должен содержать символ "@", попробуйте ещё раз')
#         return user_email()
#     elif email[email.find('@'):].find('.') == - 1:
#         print('Адрес должен оканчиваться на ".ru/.com/.bk и т.д.", попробуйте ещё раз')
#         return user_email()
#     for i in range(len(email)):
#         if not ord(email[i]) in range(32, 127):
#             print('В адресе буквы должны быть на латинице, попробуйте ещё раз')
#             return user_email()
#     else:
#         return email
#
#
# def user_phone():
#     """ Запрашивает и проверяет номер мобильного телефона по РФ образцу"""
#     try:
#         phone = int(input('Введите номер телефона (10 или 11 цифр) : '))
#         if (len(str(phone)) < 10) or (len(str(phone)) > 11):
#             print('Прожалуйста, введите корректный номер телефона')
#             return user_phone()
#         elif len(str(phone)) == 10:
#             phone = str(phone)
#             return f'+7({phone[:3]}){phone[3:6]}-{phone[6:8]}-{phone[8:]}'
#         elif len(str(phone)) == 11:
#             phone = str(phone)[1:]
#             return f'+7({phone[:3]}){phone[3:6]}-{phone[6:8]}-{phone[8:]}'
#     except ValueError:
#         print('Необходимо ввести только цифры')
#         return user_phone()
#
#
# def user_data(name, surname, birth, city, email, phone):
#     return name.capitalize(), surname.capitalize(), birth, city.capitalize(), email, phone
#
#
# n = input('Введите имя пользователя : ')
# s = input('Введите фамилию пользователя : ')
# b = birthday()
# c = input('Введите город проживания пользователя : ')
# e = user_email()
# p = user_phone()
#
# user = user_data(name=n, surname=s, birth=b, city=c, email=e, phone=p)
#
# print(f'Товарищ {user[0]} {user[1]} родился {user[2]}, проживает в городе {user[3]}.'
#       f' Адрес электронной почты : {user[4]}, номер телефона: {user[5]} ', end='\n' * 2)

# _____________________ Задание 3 ()
print('Задание №3 ↓')

# _____________________ Задание 4 ()
print('Задание №4 ↓')

# _____________________ Задание 5 ()
print('Задание №5 ↓')

# _____________________ Задание 6 ()
print('Задание №6 ↓')
