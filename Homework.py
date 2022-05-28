import re
import json


def get_file_name(task_number='_unknown', extension='txt'):
    """ Запрашивает у пользователя название файла и проверяет его на корректность
        в качестве необязательных аргументов принимает номер задания и расширение
        на случай автоматического создания файла"""

    print(
        f'Введите имя файла с расширением. Либо нажмите Enter и имя файла будет '
        f'задано автоматически как "task{task_number}.{extension}')
    task_number = task_number
    file_name = input('Введите имя файла : ')
    if file_name == '':
        return f'task{task_number}.{extension}'
    else:
        for i in file_name:
            if '<>"/|\?*:'.find(i) != -1:
                print('В названии файла есть недопустимый символ')
                return get_file_name().strip()
        if file_name.find('.') == -1:
            print('Необходимо также указать расширение файла после "." ')
            return get_file_name(task_number)
        else:
            last_point_index = len(file_name) - 1 - file_name[::-1].index('.')  # на случай, если точек в файле > 1
            name, extension = file_name[:last_point_index], file_name[last_point_index + 1:]
            if extension == '':
                print('Расширение файла не может быть пустым')
                return get_file_name(task_number)
            elif len(name) != len(name.strip()):
                print('Название файла не должно содержать пробел в конце')
                return get_file_name(task_number)
            elif name.upper() in 'CON, PRN, AUX, NUL, COM1, COM2, COM3, COM4, COM5, ' \
                                 'COM6, COM7, COM8, COM9, LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, LPT9':
                print(f'Введите другое имя файла. Значение {name} зарезервировано системой')
                return get_file_name(task_number)
            else:
                return file_name.strip()


# ______________________ Задание 1 (Создать файл, записать данные от пользователя, зыкрыть по пустой строке)
print('Задание №1 ↓')

file_name = get_file_name(1)
with open(file_name, 'w', encoding='utf-8') as f:
    print(f'Программа построчно запишет введённые Вами данные в файл {file_name}'
          '. Для прекращения ввода нажмите Enter (без самих данных)')
    user_input_list = []
    while True:
        text = input('Введите данные : ')
        if text == '':
            break
        else:
            user_input_list.append(text)
    print(*user_input_list, sep='\n', end='', file=f)

print('\n\n')

# _____________________ Задание 2 (Прочитать готовый файл и посчитать количество строк и слов)
print('Задание №2 ↓')

with open('cat_verse.txt', encoding='utf-8') as f:
    li_lines = f.readlines()
    print(f'В файле cat_verse.txt строк : {len(li_lines)} ')
    for i, line in enumerate(li_lines, 1):
        print(f'В {i}-й строке слов: {len(line.split())}')

print('\n\n')

# _____________________ Задание 3 (Прочитать готовый файл с фамилиями и з/п, вывести всех с з/п ниже 20к, среднюю з/п)
print('Задание №3 ↓')

with open('staff_salary.txt', encoding='utf-8') as f:
    li_staff = [i.strip().split() for i in f.readlines()]
    total_salary = 0

    print('Сотрудники, чей оклад меньше 20000 ↓')
    for i in range(len(li_staff)):
        total_salary += float(li_staff[i][1])
        if float(float(li_staff[i][1]) < 20_000):
            print(li_staff[i][0])
    print(f'\nСредняя з/п : {round(total_salary / len(li_staff), 2)}', end='\n\n')

# _____________________ Задание 4 (Прочитать построчно готовый файл, поменять английские слова на русские)
print('Задание №4 ↓')

file_name = get_file_name(4)
en_ru_numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('numbers.txt', encoding='utf-8') as f:
    li_numbers = [[i for i in j.split('—')] for j in f.readlines()]
    with open(file_name, 'w', encoding='utf-8') as f_out:
        for i in range(len(li_numbers)):
            li_numbers[i] = en_ru_numbers[li_numbers[i][0].strip()] + " —" + li_numbers[i][1]
            f_out.write(li_numbers[i])

print(f'В файл {file_name} записаны переработанные данные из файла numbers.txt ', end='\n\n')

# _____________________ Задание 5 (Создать файл, записать в него набор чисел)
print('Задание №5 ↓')


def get_number_list(n):
    """ Запрашивает у пользователя набор чисел, разделённых пробелом.
        Проверяет введённые данные на корректность
        В качестве аргумента принимает номер итерации функции"""
    n = n
    flag = True
    user_input = input(f'Введите {n}-й набор чисел : ').lower()
    if user_input == '':
        print('Введена пустая срока. Введите набор чисел или stop для завершения ввода')
        return get_number_list(n)
    if 'stop' in user_input:
        print('Введено слово stop, ввод данных прекращается')
        user_input = user_input.replace('stop', '')
        flag = False
    try:
        lst_numbers = [float(i) for i in user_input.strip().split()]
        return lst_numbers, flag
    except ValueError:
        print('Необходимо вводить только числовые значения! ')
        return get_number_list(n)


file_name = get_file_name(5)
with open(file_name, 'w', encoding="utf-8") as f:
    n = 0
    li_total = []
    flag = True
    print('Введите последовательность чисел через пробел. Или stop, чтобы завершить ввод. ')
    while flag:
        n += 1
        li_temporary, flag = get_number_list(n)
        if li_temporary:
            li_total.append(li_temporary)
    for j in range(len(li_total)):
        if j + 1 == len(li_total):
            f.writelines(' '.join([str(i) for i in li_total[j]]))
        else:
            f.write(' '.join([str(i) for i in li_total[j]]) + '\n')
    print(f'В файл {file_name} добавлены все Ваши цифровые строки.'
          f' Сумма всех цифр = {round(sum([sum(i) for i in li_total]), 2)}', end='\n\n')

# _____________________ Задание 6 (Прочитать файл, создать из данных словарь)
print('Задание №6 ↓')

with open('curriculum.txt', encoding='utf-8') as f:
    li_curriculum = f.readlines()
    dic_curriculum = {}
    for i in range(len(li_curriculum)):
        s = li_curriculum[i]
        dic_curriculum[s[:s.index(':')]] = sum([int(i) for i in re.findall(r'\d+', s)])
    print('Словарь, созданный из данных файла curriculum.txt имеет следующий вид:\n', dic_curriculum, end='\n\n')

# _____________________ Задание 7 (Прочитать файл с данными о компании, вычислить прибыли и вывести в словарь )
print('Задание №7 ↓')

with open('companies.txt', encoding='utf-8') as f:
    f_count = 0  # количество компаний
    f_sum = 0  # сумма прибыли доходных компаний
    f_dict = {}  # словарь "компания": прибыль
    average_profit = {}  # словарь "средняя прибыль" : средняя прибыль
    for line in f.readlines():
        firm_name, s, profit, losses = line.strip().split()
        f_dict[firm_name] = int(profit) - int(losses)
        if int(profit) > int(losses):
            print(f'Прибыль компании {firm_name} составила: {int(profit) - int(losses)} у.е.')
            f_count += 1
            f_sum += int(profit) - int(losses)
        elif int(profit) < int(losses):
            print(f'Убыток компании {firm_name} составил: {int(losses) - int(profit)} у.е.')
        else:
            print(f'Компания {firm_name} работает в ноль')
    try:
        average_profit['average_profit'] = round(f_sum / f_count, 2)
        print(f'Средняя прибыль среди доходных компаний составила: {average_profit["average_profit"]} у.е.')
    except ZeroDivisionError:
        print('Все компании из списка убыточны')
        average_profit['average_profit'] = 0
    file_name = get_file_name(7, 'json')
    with open(file_name, 'w', encoding='utf-8') as f_out:
        json.dump([f_dict, average_profit], f_out)
        print(f'В файл {file_name} записана информация в формате json')
