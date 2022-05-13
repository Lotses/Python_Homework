# #_____________________ Задание 1 (Вводим данные в переменные и выводим)
# print('Задание №1 ↓')
# cat_name = input('Введите имя кота: ')
# expenses = input('Введите сколько рублей кот тратит на корм: ')
# print(f'Ваш кот {cat_name.capitalize()} очень наглый, он тратит аж {expenses} рублей на корм')
# print()

# #_____________________ Задание 2 (вводим секунды и выводим в формате чч:мм:сс)
# class DateTime(): # Создаём класс и функцию для вывода в формате чч:мм:сс (если значение меньше 10, то выведется 0Ч:0М:0С)
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def display(self):
#         print(f'Введённое количество секунд соответствует {self.hours:02}:{self.minutes:02}:{self.seconds:02}')
#
# print('Задание №2 ↓')
# seconds = int(input('Введите количество секунд: '))
# hours = seconds // 3600
# minutes = (seconds % 3600) // 60
# sec = (seconds % 3600) % 60
#
# time_1 = DateTime(hours, minutes, sec)
# time_1.display()
# print()

# #_____________________ Задание 3 (Вводим число n и выводим сумму n + nn + nnn)
# print('Задание №3 ↓')
# number = int(input('Введите целое число до 10: '))
# print('Результат n + nn + nnn = ', number + number * 11 + number * 111)
# print()

# #_____________________ Задание 4 (Вводим целое положительное число, находим самую большую цифру)
# print('Задание №4 ↓')
# number = int(input('Введите целое положительное число: '))
# max_number = 0
# while number != 0:
#     if max_number < number % 10:
#         max_number = number % 10
#     number //= 10
# print('Самая большая цифра в числе: ', max_number)
# print()

#_____________________ Задание 5 (Вводим два числа, сравниваем какое больше)
print('Задание №5 ↓')
earnings, costs = float(input('Введите сумму доходов: ')), float(input('Введите сумму затрат: '))
if earnings > costs:
    print(f'Компания приносит доход! Чистая прибыль составила {earnings - costs} у.е.')
elif costs > earnings:
    print(f'Компания не приносит доход! Сумма убытков составила {costs - earnings} у.е.')
else:
    print('Компания на грани окупаемости, сумма доходов равна сумме затрат')
print()