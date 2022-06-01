import time
import random


# ______________________ Задание 1 (Класс светофор)_____________________________________________________

class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']
    color_time = [4, 7, 2]

    def __init__(self, user_colour):
        """ Конструктор. Принимает аргумент - стартовый цвет светофора"""
        if user_colour == "":
            user_colour = 'красный'
        self.__start = TrafficLight.__color.index(user_colour)

    def running(self):
        """ Переключает цвет светофора на следующий """
        if self.__start < 2:
            self.__start += 1
        else:
            self.__start = 0
        return TrafficLight.__color[self.__start], TrafficLight.color_time[self.__start]


# # _____________________ Задание 2 (Класс Road)________________________________________________________

class Road:
    def __init__(self, length, width):
        """ Конструктор, принимает параметры класса длину и ширину асфальтового покрытия"""
        self._length = length
        self._width = width

    def asphalt_mass(self, m_mass, m_deep):
        """ Рассчитывает массу асфальтового покрытия, принимает два дополнительных аргумента:
            массу покрытия на 1м.кв и глубину покрытия"""
        return round(self._length * self._width * m_mass * m_deep, 2)


# # _____________________ Задание 3 (Класс Worker)______________________________________________________

class Worker:
    def __init__(self, name, surname, position):
        self.name = ('Джон', name)[name != '']
        self.surname = ('Смит', surname)[surname != '']
        self.position = ('агент', position)[position != '']
        self._income = {"Оклад": 14000, "Премия": 10000}


class Position(Worker):

    def get_full_name(self):
        """ Возвращает объединённые строки Name и Surname"""
        return self.name + " " + self.surname

    def get_total_income(self):
        """ Возвращает суммарный доход работника (Оклад + Премия) """
        return self._income["Оклад"] + self._income["Премия"]


# # _____________________ Задание 4 (Class Car & дочки)__________________________________________________
# print('Задание №4 ↓')

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = (60, speed)[speed != '']
        self.color = ('Чёрный', color)[color != '']
        self.name = ('Волга', name)[name != '']
        self.is_police = (True, is_police)[is_police != '']

    def go(self):
        """ запуск автомобиля"""
        return 'рванула с места'

    def stop(self):
        """ остановка автомобиля"""
        return "Машина остановилась"

    def turn(self, direction):
        """ поворот автомобиля"""
        self.direction = direction
        return f'{self.direction}'

    def show_speed(self):
        """ Возвращает скорость ТС"""
        return f'{self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        """ Возвращает скорость ТС и предупреждение о превышении 60 км/ч"""
        if self.speed > 60:
            return f' {self.speed}км/ч, что больше разрешённой 60км/ч.'
        return f'{self.speed} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    """ Возвращает скорость ТС и предупреждение о превышении 40 км/ч"""

    def show_speed(self):
        if self.speed > 40:
            return f' {self.speed}км/ч, что больше разрешённой 40км/ч.'
        return f'{self.speed} км/ч'


class PoliceCar(Car):
    pass


# # _____________________ Задание 5 (Канцелярия и дочки)_________________________________________________
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        """ печатает фразу 'Запуск отрисовки' """
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'"Мы - {self.title} обведённые узоры.')


class Pencil(Stationery):
    def draw(self):
        print(f'Заполнены цветным {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'И {self.title} отмеченные поры,\n'
              'Куда удобнее достать ножом"\n')


#
# # _______________________________ необходимые внеклассовые функции______________________________________


def traffic_colour_input():
    """Запрашивает у пользователя исходный цвет светофора и проверяет на корректность.
        Цвета должны быть: красный/ зелёный/ жёлтый"""
    start_colour = input("Введите цвет светофора: ").strip().lower()
    start_colour = start_colour.replace('лен', 'лён')
    start_colour = start_colour.replace('жел', 'жёл')
    if start_colour == "":
        return 'красный'
    elif start_colour not in ["красный", "жёлтый", "зелёный", ]:
        print('Такого цвета у светофора нет')
        return traffic_colour_input()
    else:
        return start_colour


def color_print(color):
    """ В качестве аргумента принимает цвет, который нужно напечатать и выводит его в соответствующем цвете"""
    if color == 'зелёный':
        print("\033[32m {}\033[0m".format(color), end=' ')
    elif color == 'красный':
        print("\033[31m {}\033[0m".format(color), end=' ')
    elif color == 'жёлтый':
        print("\033[33m {}\033[0m".format(color), end=' ')


def get_len_wid():
    """ Запрашивает и проверяет длину и ширину покрытия"""
    try:
        length, width = input('Введите длину дороги, по которой будет ехать персонаж, в метрах : '), \
                        input('Введите ширину дороги, по которой будет ехать персонаж, в метрах : ')
        if length == '':
            length = 1000
        if width == '':
            width = 5
        if (length == 0.0) or (width == 0.0):
            raise ValueError
        length, width = float(length), float(width)
        return abs(length), abs(width)
    except ValueError:
        print('Необходимо ввести числа, также недопустим 0')
        return get_len_wid()


def get_weight_deep():
    """ Запрашивает и проверяет вес на 1м.кв. и глубину покрытия в см"""
    try:
        weight, deep = input('Введите вес полотна дороги в кг на 1 квадратный метр : '), \
                       input('Введите глубину асфальтового покрытия в см. : ')
        if weight == '':
            weight = 25
        if deep == '':
            deep = 5
        if (weight == 0.0) or (deep == 0.0):
            raise ValueError
        weight, deep = float(weight), float(deep)
        return abs(weight), abs(deep)
    except ValueError:
        print('Необходимо ввести числа, также недопустим 0')
        return get_weight_deep()


def get_car_info():
    """ Запрашивает у пользователя и проверяет на корректность данные: скорость, цвет, название, полиция, направление"""
    auto_li = ["спортивная", "обычная", "рабочая"]
    try:
        speed = input('Введите скорость авто главного героя (цифра в км/ч): ')
        if speed != '':
            speed = float(speed)
        is_police = input('Задействовать в рассказе полицейскую машину? да/нет : ').lower()
        if is_police != '':
            is_police = (False, True)[is_police == 'да']
        else:
            is_police = True
        user_car_type = input('Выберите на какой машине будет ездить главный герой '
                              '(Спортивная/ Обычная/ Рабочая) : ').lower()
        if user_car_type in auto_li:
            user_car_type = auto_li.index(user_car_type)
        else:
            user_car_type = ''
        user_car_name = input('Введите название/марку автомобиля : ')
        user_color_name = input('Введите цвет автомобиля : ')
        user_direction = input('Введите направление судьбоносного поворота авто (лево/право) : ').lower()
        if user_direction not in ('лево', 'право'):
            user_direction = random.choice(['лево', 'право'])
        return speed, user_color_name.capitalize(), user_car_name.capitalize(), is_police, user_direction, user_car_type
    except ValueError:
        print('Скорость автомобиля должна быть введена в виде числа')
        return get_car_info()


# __________________________________основной код____________________________________________________________

choice = input(
    'Программа предложит Вам поучаствовать в небольшом интерактивном рассказе (10 минут), где Вы сможете стать '
    'соавтором.\n Введите "да" если хотите узнать подробности, или нажмите enter, чтобы начать ввод данных : ')
if choice.lower() == 'да':
    print('В самом начале программа попросит Вас ввести базовые данные для составления рассказа.\n'
          'Также, во время самого рассказа вы можете увидеть такую конструкцию: "[text/ text_2]",\n'
          'это означает, что Вам необходимо сделать выбор из двух предложенных вариантов.\n'
          'Если у Вас нет желания вводить информацию, то просто нажимайте Enter, и значения будут подстав -\n'
          'лены за Вас. Программа будет сама регулировать время вывода текста. Когда вы прочтёте очередное\n'
          'предложение, не нужно никуда нажимать, просто дождитель следующего. Помните, что от Вашего выбора \n'
          'зависит судьба главного героя, и только Вам решать куда его заведут судьбоносные повороты жизненной тропы.\n'
          '_____________________  Пора в путь !____________________')
else:
    print('Сначала необходимо ввести базовый набор данных (Вы всегда можете нажать Enter'
          ' и значения введутся автоматически)')
time.sleep(1)

worker = Position(input('Введите имя главного героя : ').capitalize(), input('Введите фамилию : ').capitalize(),
                  input('Введите должность : '))

*args, car_direction, car_type = get_car_info()
if car_type == 0:
    main_car = SportCar(*args)
elif car_type == 1:
    main_car = TownCar(*args)
else:
    main_car = WorkCar(*args)

co = traffic_colour_input()
traffic = TrafficLight(co)

le, wi = get_len_wid()
we, de = get_weight_deep()

good_points, bad_points = 0, 0
delay = 7

print('Начинаем рассказ: ')
time.sleep(2)
print(f' Размеренный и почти убаюкивающий гул мегаполиса-N нарушал натужный рёв двигателя.')
time.sleep(delay)
print(f'{main_car.color} автомобиль мчался по шоссе, рассекая мерцающую мглу ночного города.')
time.sleep(delay - 2)
print(f'За рулём машины {main_car.name} сидел {worker.position} {worker.get_full_name()}. ')
time.sleep(delay - 2)
print(f'На его лице застыла маска уверенного равнодушия. Похоже что таким должно быть лицо человека,\n'
      f'решившегося на опрометчивый судьбоносный проступок.')
time.sleep(delay + 3)
print(f'И хотя лицо {worker.name}a выражало стойкость злонамерений, внутри, однако, бушевал ураган эмоций,\n'
      f'сомнений и мытарства.')
time.sleep(delay + 4)
print(f'В голове попеременно мелькали мысли, образы, воспоминания. Но возглавлял сие сумасшествие'
      f' всего один вопрос: ', end=' ')
choice_1 = input('[убить или пощадить?]')
time.sleep(2)
if choice_1.lower() == 'пощадить':
    good_points += 1
    print(f'Или быть может наоборот, обрушить длань на мерзкого предателя? И снова несуразные воспоминания'
          f' повылезали из тени сознания.')
else:
    bad_points += 1
    print(f'Или быть может наоборот, простить и забыть всё как страшный сон? И снова несуразные воспоминания'
          f' повылезали из тени сознания:')
time.sleep(delay + 4)
road = Road(le, wi)
print(f'"{worker.name}!" - закричал начальник инженерно-рассчётного отдела - "Давай, давай, просыпай свои извилины.\n'
      f'У нас заказ на {road._length} x {road._width} метров дороги, марка 3, глубина {de}. Мне нужен тоннаж, быстро!"')
time.sleep(delay + 6)
print(f'10 лет, отданных сфере строительства прошли не зря. Результат в {road.asphalt_mass(we, de)} тонн мгновенно\n'
      f'всплыл в голове. Когда-то зарплата в {worker.get_total_income()} вызывала гордость. А сейчас... это не важно.')
time.sleep(delay + 6)
print(f'Моргающий {co.lower()} цвет приближающегося светофора вывел водителя из своих мыслей.\n'
      f'Больше всего {worker.name} не любил ждать. Секции светофора нарочито неспешно сменяли друг-друга:', end=' ')
time.sleep(3)
color_print(co)
while True:
    color, time_delay = traffic.running()
    time.sleep(time_delay)
    color_print(color)
    if color == 'зелёный':
        break
time.sleep(delay - 4)
print()
print(f'Машина завелась, {main_car.go()}, с визгом вписалась в поворот на{main_car.turn(car_direction)} '
      f'и стала набирать скорость.')
time.sleep(delay + 1)
print(f'Скорость автомобиля достигла {main_car.show_speed()}.')
time.sleep(delay - 2)
if main_car.is_police:
    print('Сзади послышался пронзительный вой полицейской сирены. Рука безвольно легла на '
          'холодный ствол Beretta 92', end=' ')
    choice_1 = input('[выстрелить или оторваться?]')
    time.sleep(2)
    if choice_1.lower() == 'оторваться':
        good_points += 1
        print(f'Решив не усугублять и без того мрачное положение {worker.name} резко вывернул руль'
              f' и скрылся в паутине местного гетто.')
    else:
        bad_points += 1
        print(f'{worker.name} вслепую произвёл несколько выстрелов в сторону полицейской машины. Одна из пуль,\n'
              f' срикошетив, задела случайного прохожего. Но от погони удалось уйти.')
    time.sleep(delay + 3)
print(f'Стрелки часов перевалили за полночь, улицы опустели, а наш герой достиг места назначения.\n'
      f'{main_car.stop()} у небольшого кирпичного дома.')
time.sleep(delay + 3)
print(f'{worker.name} отсутствующим взглядом буравил скомканную записку. Ту самую, что оставила Джессика,\n'
      f'на подушке в их спальне, после чего собрала все вещи и исчезла без следа.')
time.sleep(delay + 3)
text_1 = Pen('ручкой')
text_2 = Pencil('карандашом')
text_3 = Handle('маркером')
print(f'На записке, замысловатым бегущим почерком были выведены строки:\n')
time.sleep(delay)
text_1.draw()
time.sleep(delay - 3)
text_2.draw()
time.sleep(delay - 3)
text_3.draw()
time.sleep(delay - 3)

print(f'Джессика всегда любила изъясняться загадками. Но подпись на обратной стороне'
      f' не оставляла пространства для фантазий :\n'
      f'"{worker.name}, всё зашло слишком далеко, прощай. Я ухожу к Тому"')
time.sleep(delay + 5)
print('Глаза снова налились кровью, а гнев разжёг всепоглащающее пламя ненависти.\n'
      'Что сделать с этой проклятой запиской, перевернувшей мир вверх дном?', end=' ')
choice_1 = input('[выбросить или оставить?]')
time.sleep(2)
if choice_1.lower() == 'оставить':
    good_points += 1
    print(f'Пускай этот клочок бумаги послужит вечным памятником предательства. И всякий раз будет напоминать о том,\n'
          f'что этот мир не сказка. {worker.name} вытащил из бардачка свёрнутый кусок ткани, '
          f'развернул его и достал содержимое.')
else:
    bad_points += 1
    print(f'Предательский клочок бумаги был снова скомкан и выброшен в окно. Начиная с этой секунды он перестал '
          f'представлять\n из себя хоть что-то значимое и важное. {worker.name} вытащил из бардачка свёрнутый кусок '
          f'ткани, \nразвернул его и достал содержимое.')
time.sleep(delay + 4)
print('Beretta лежала в руке продолжением оной. Холодная и увесистая, она, пожалуй, олицетворяла ту часть человека,\n'
      'которая всегда мечтала быть выше, сильнее, быть первым и единственным. Вершитель судеб и гарант справедливости.')
time.sleep(delay + 6)
print('Отец учил, что ложь красной нитью подвязана под каждое слово. И всё что остаётся нам - это', end=' ')
choice_1 = input('[верить или не верить?]')
time.sleep(2)
if choice_1.lower() == 'не верить':
    good_points += 1
    print(f'А значит, виноват ли кто-то в моей ошибке?')
else:
    bad_points += 1
    print(f'И я поверил. Выходит что зря.')
time.sleep(delay - 1)
print(f'В окне кирпичного дома два силуэта задорно кружились в танце беззаботного неведения.\n'
      f'{worker.name} наблюдал за Джессикой и Томом. И никакие сомнения более не терзали разум.')
time.sleep(delay + 5)
if good_points > bad_points:
    print(' Размеренный и почти убаюкивающий гул мегаполиса-N нарушал натужный рёв двигателя.')
    time.sleep(delay)
    print(f'{main_car.color} автомобиль мчался по шоссе, рассекая мерцающую мглу ночного города.')
    time.sleep(delay)
    print(f'За рулём машины {main_car.name} сидел {worker.position} {worker.get_full_name()}.\n'
          f'И он оставил позади обиды, месть и сожаления.')
    time.sleep(delay)
    print(f'Впереди прекрасный день, свободный от оков гнева и последствий. {worker.name} свободен.')
elif good_points < bad_points:
    print(' Размеренный и почти убаюкивающий гул мегаполиса-N нарушал натужный рёв двигателя.')
    time.sleep(delay)
    print(f'{main_car.color} автомобиль мчался по шоссе, рассекая мерцающую мглу ночного города.')
    time.sleep(delay)
    print(f'За рулём машины {main_car.name} сидел {worker.position} {worker.get_full_name()}.\n'
          f'Человек, утопивший своё горе в крови обидчиков.')
    time.sleep(delay)
    print(f'Впереди лишь клеймо убийцы, вечные погони и стенания души. {worker.name} обречён.')
else:
    print(' Размеренный и почти убаюкивающий гул мегаполиса-N нарушал натужный рёв двигателя.')
    time.sleep(delay)
    print(f'Автомобиль скорой помощи мчался по шоссе, рассекая мерцающую мглу ночного города.')
    time.sleep(delay + 2)
    print(f'За рулём машины {main_car.name} сидел {worker.position} {worker.get_full_name()}.\n'
          f'Запятнанный кровью салон мгновенно пропитался запахом смерти. ')
    time.sleep(delay + 3)
    print(f'Рано или поздно оружие всегда забирает чью-то жизнь. {worker.name} отдал свою.')
time.sleep(delay)
print('_______КОНЕЦ______Спасибо за удлённое время!')
