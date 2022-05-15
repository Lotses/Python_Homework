#_____________________ Задание 1 (Создаём список с разными типами данных и циклом выводим типы элементов)
print('Задание №1 ↓')
li = [1, 'Кот', True, 12.3, [1, 2, 3, 4], (1, 2, 3, 4),
      {'Кот': 'уши, лапы, хвост', 'Морская свинка': 'уши, лапы, "уип-уип"'},
      {1, 2, 3, 4}]

for i in range(len(li)):
    print(li[i], type(li[i]))
print()


#_____________________ Задание 2 (Обмен соседних значений в списке)
print('Задание №2 ↓')
li = input('Введите элементы списка через пробел (прим. "1 2 3 ..."): ').split()

for i in range(0, len(li), 2):
    if i + 1 == len(li):
        break
    li[i], li[i + 1] = li[i + 1], li[i]

print(f'Соседние значения списка изменены: {" ".join(li)}', end='\n' * 2)


#_____________________ Задание 3 (Определяем время года через список и словарь)
print('Задание №3 ↓')

month = int(input('Введите порядковый номер месяца (от 1 до 12): '))
                    # Решение через словарь:

season_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

for i in season_dict:
    if month in season_dict[i]:
        print(f'Этот месяц относится к времени года: {i}')
        break
                    # Решение через список, 1-й вариант:

season_list = ['Зима', 'Весна', 'Лето', 'Осень']

if month == 12:
    month = 2

print(f'Этот месяц относится к времени года: {season_list[month // 3]}')
                    # Решение через список, 2-й вариант:

season_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
print(f'Этот месяц относится к времени года: {season_list[month - 1]}', end='\n' * 2)


#_____________________ Задание 4 (Вывести список построчно с нумерацией элементов)
print('Задание №4 ↓')

text = input('Введите предложение: ').split()
for i, element in enumerate(text, 1):
    print(f'{i}-e слово: {element[:10]}')

print()
#_____________________ Задание 5 (Структура "Рейтинг")
print('Задание №5 ↓')
my_list = [7, 5, 3, 3, 2]
number = int(input('Введите число: '))

for i in range(len(my_list)):
    if number > my_list[i]:
        my_list.insert(i, number)
        print('Число вставлено в начало. Результат: ', end='')
        break
    elif i + 1 == len(my_list):
        my_list.append(number)
        print('Число вставлено в конец. Результат: ', end='')
        break
    elif my_list[i] >= number > my_list[i + 1]:
        my_list.insert(i + 1, number)
        print(f'Число вставлено в {i}-й элемент. Результат: ', end='')
        break
print(*my_list, end='\n' * 2)


#_____________________ Задание 6 (Создаём структуру "Товары")
print('Задание №6 ↓')
goods_list = []         # задаём пустой список
goods_dict = {}         # задаём пустой словарь
terminate = 'да'          # задаём переменную для завершения цикла пользователем
i = 0                   # задаём переменную счётчика

while terminate == 'да':
    i += 1
    goods_dict['название'] = input('Введите название товара: ')
    goods_dict['цена'] = input('Введите цену товара: ')
    goods_dict['количество'] = input('Введите количество товара: ')
    goods_dict['ед'] = input('Введите единицу измерения товара: ')
    goods_list.append((i, goods_dict.copy()))
    terminate = input(f'Вы ввели товаров: {i}, хотите продолжить? да/нет: ').lower()
print(f'{"_" * 25}Таблица товаров имеет следующий вид:{"_" * 25}')
print(*goods_list, sep='\n')
                # выводим аналитику
goods_dict.clear()
goods_dict['название'] = [goods_list[i][1]['название'] for i in range(i)]
goods_dict['цена'] = [goods_list[i][1]['цена'] for i in range(i)]
goods_dict['количество'] = [goods_list[i][1]['количество'] for i in range(i)]
goods_dict['ед'] = list(set([goods_list[i][1]['ед'] for i in range(i)]))
print(f'{"_" * 25}Данные для аналитики:{"_" * 40}')
for key, values in goods_dict.items():
    print(f'{key} : {values}')
