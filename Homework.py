import datetime


class TerminateProg(Exception):
    pass


# _____________________ Задание 1 (Запрашивать два числа, поделить, проверить знаменатель на ноль)
print('Задание №1 ↓')


def division():
    """
    Запрашивает два числа и делит одно число на другое

    () -> input(number), input(number) -> number
    >>> division() -> 10, 2
    5
    """

    try:
        num1 = input('Введите числитель : ')
        if num1 == '%':
            raise TerminateProg
        num2 = input('Введите знаменатель : ')
        if num2 == '%':
            raise TerminateProg
        return f' Результат деления: {round(float(num1) / float(num2), 2)}'
    except TerminateProg:
        return "Введён символ %, программа завершает работу."
    except ZeroDivisionError:
        print('На ноль делить нельзя! Давайте попробуем ещё раз (или введите "%" для завершения):')
        return division()
    except ValueError:
        print('Необходимо ввести число! Давайте попробуем ещё раз (или введите "%" для завершения):')
        return division()


print(division(), end='\n' * 2)

# _____________________ Задание 2 (Собрать данные о пользователе через именнованные аргументы и вывести одной строкой)
print('Задание №2 ↓')


def birthday():
    """ Забирает от пользователя год, месяц и день рождения, проверяет на корректность данных.
        На каждый показатель (день, месяц и год) объявляется своя функция для проверки верности
        введённых данных. Это позволяет не заставлять пользователя каждый раз вводить все данные,
        а исправлять только неверные.
    """

    def date_year():
        """ Получает и обрабатывает год рождения """
        try:
            year = int(input('Введите год рождения в формате уууу : '))
            if len(str(year)) < 4:
                print('Пожалуйста, введите год в формате уууу')
                return date_year()
            if (datetime.datetime.now().year - year) > 122:
                print(f'Вряд ли пользователю {datetime.datetime.now().year - year} лет, попробуйте ещё раз')
                return date_year()
            elif datetime.datetime.now().year < year:
                print('Человек ещё не родился, попробуйте ещё раз')
                return date_year()
            return year
        except ValueError:
            print('Необходимо ввести число, давайте попробуем ещё раз')
            return date_year()

    def date_month():
        """ Получает и обрабатывает месяц рождения """
        month_ru = {'январь': '01', 'февраль': '02', 'март': '03', 'апрель': '04', 'май': '05', 'июнь': '06',
                    'июль': '07', 'август': '08', 'сентябрь': '09', 'октябрь': '10', 'ноябрь': '11', 'декабрь': '12',
                    }
        month = input('Введите месяц рождения : ').lower()
        if month.isalpha():
            if month in month_ru:
                return month_ru[month]
            else:
                print('Такого месяца не существует, попробуйте ещё раз')
                return date_month()
        elif month.isnumeric():
            if (int(month) > 12) or (int(month) < 1):
                print('Такого месяца не существует, попробуйте ещё раз')
                return date_month()
            else:
                return int(month)
        else:
            print('Введён неверный формат месяца : ')
            return date_month()

    def date_day():
        """ Получает и обрабатывает день рождения """
        day = int(input('Введите день рождения : '))
        try:
            if (day > 31) or ((int(d_m) == 2) and (day > 29)) or (day < 1):
                print('Такого числа нет в месяце, попробуйте ещё раз')
                return date_day()
            return day
        except ValueError:
            print('Пожалуйста, введите цифры дня :')
            return date_day()

    d_m = date_month()
    return f'{date_day():02}.{d_m:02}.{date_year()}'


def user_email():
    """ Запрашивает и проверяет на корректность адрес электронной почты """
    email = input('Введите адрес электронной почты : ')
    if not '@' in email:
        print('Адрес должен содержать символ "@", попробуйте ещё раз')
        return user_email()
    elif email[email.find('@'):].find('.') == - 1:
        print('Адрес должен оканчиваться на ".ru/.com/.bk и т.д.", попробуйте ещё раз')
        return user_email()
    for i in range(len(email)):
        if not ord(email[i]) in range(32, 127):
            print('В адресе буквы должны быть на латинице, попробуйте ещё раз')
            return user_email()
    else:
        return email


def user_phone():
    """ Запрашивает и проверяет номер мобильного телефона по РФ образцу"""
    try:
        phone = int(input('Введите номер телефона (10 или 11 цифр без пробела) : '))
        if (len(str(phone)) < 10) or (len(str(phone)) > 11):
            print('Прожалуйста, введите корректный номер телефона')
            return user_phone()
        elif len(str(phone)) == 10:
            phone = str(phone)
            return f'+7({phone[:3]}){phone[3:6]}-{phone[6:8]}-{phone[8:]}'
        elif len(str(phone)) == 11:
            phone = str(phone)[1:]
            return f'+7({phone[:3]}){phone[3:6]}-{phone[6:8]}-{phone[8:]}'
    except ValueError:
        print('Необходимо ввести только цифры без пробела')
        return user_phone()


def user_data(name, surname, birth, city, email, phone):
    return name.capitalize(), surname.capitalize(), birth, city.capitalize(), email, phone


n = input('Введите имя пользователя : ')
s = input('Введите фамилию пользователя : ')
b = birthday()
c = input('Введите город проживания пользователя : ')
e = user_email()
p = user_phone()

user = user_data(name=n, surname=s, birth=b, city=c, email=e, phone=p)

print(f'Товарищ {user[0]} {user[1]} родился {user[2]}, проживает в городе {user[3]}.'
      f' Адрес электронной почты : {user[4]}, номер телефона: {user[5]}.\n'
      f'Подозревается в мошенничестве в особо крупном размере. За ним выехали.', end='\n' * 2)

# _____________________ Задание 3 (Запросить три аргумента и вывести сумму двух наибольших)
print('Задание №3 ↓')


def my_func(a, b, c):
    """ Принимает три значения и возвращает сумму двух наибольших"""
    lst = sorted([a, b, c], reverse=True)
    try:
        return int(lst[0]) + int(lst[1])
    except ValueError:
        return lst[0] + lst[1]


a, b, c = input('Введите первый аргумент : '), input('Введите второй аргумент : '), input('Введите третий аргумент : ')
print(f'Результат сложения двух наибольших значений : {my_func(a, b, c)}', end='\n' * 2)

# _____________________ Задание 4 (Запросить х (действительное положительное) и возвести в степень у (целое отриц.))
print('Задание №4 ↓')


def input_xy():
    """ Запрашивает действительное положительное число х, затем вызывает функцию запроса числа y
        Также проверяет числа на соответствие условию. Если всё ок, возвращает эти числа
    """

    def input_y():
        """ Запрашивает у, проверяет что он целый и отрицательный (Ноль тоже отрицательный!)"""
        try:
            y = int(input('Введите целое отрицательное число у : '))
            if y > 0:
                print('Ваше число положительное, попробуйте ещё раз')
                return input_y()
            return y
        except ValueError:
            print('Необходимо ввести число! попробуйте ещё раз')
            return input_y()

    try:
        x = float(input('Введите действительное положительное число х : '))
        if x < 0:
            print('Ваше число отрицательное, попробуйте ещё раз')
            return input_xy()
        return x, input_y()
    except ValueError:
        print('Необходимо ввести число! Попробуйте ещё раз')
        return input_xy()


def my_func(x, y):
    """ Возводит х в степень у двумя способами"""
    num_result = x
    if y == 0:
        num_result = 1.0
    else:
        for _ in range(abs(y) - 1):
            num_result *= x
    return f'(Вариант 1) Число {x} в степени {y} = {round(x ** y, 2)}\n(Вариант 2) ' \
           f'Число {x} в степени {y} = {round(1 / num_result, 2)}'


x, y = input_xy()
print(my_func(x, y), end='\n' * 2)

# _____________________ Задание 5 (Запрашивать строку с числами и суммировать. Если введён спецсимвол, то стопорить)
print('Задание №5 ↓')


def numbers_sum(numbers):
    """ Получает список чисел и считает сумму"""
    try:
        s_num = sum(list(map(int, numbers)))
        return s_num
    except ValueError:
        print('Кажется, не все элементы строки числа. Попробуйте ещё раз')
        return 0


sum_n = 0
flag = True
while flag:
    numbers = input('Введите строку с числами, разделёнными пробелом (или "%" чтобы завершить работу) : ').split()
    if '%' in numbers:
        print('Введён спец.символ, программа будет завершена.')
        flag = False
        numbers.remove('%')
    sum_n += numbers_sum(numbers)
    print(f'Сумма всех введённых чисел = {sum_n}')

print('\n')

# _____________________ Задание 6/7 (Забираем предложение из маленьких латинских букв, выводим по одному слову)
print('Задание №6/7 ↓')


def int_func(s):
    """ Принимает предложение, возвращает его же, но первая буква каждого слова в верхнем регистре
        """
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return s


def int_input():
    """ Запрашивает у пользователя предложение и проверяет его на корректность"""
    ls = input('Введите предложение из слов через пробел (из маленьких латинских букв) : ').split()
    non_latin_count = 0
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if ord(ls[i][j]) in range(97, 123):
                pass
            else:
                non_latin_count += 1
        ls[i] = ls[i].capitalize()
    if non_latin_count != 0:
        print(f'Ваше предложение содержит {non_latin_count} символов не в латинице или в верхнем регистре.'
              f' Попробуйте ещё раз')
        return int_input()
    else:
        return ls


print(f"Переработанная строка имеет вид : {' '.join(int_func(int_input()))}")
