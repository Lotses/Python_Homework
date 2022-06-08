from time import sleep
from random import randint

# ______________________ Задание 1 ()
print('Задание №1 ↓')


class Data:
    def __init__(self, user_data):
        self.data = Data.convert(user_data)
        if self.data is None:
            pass
        else:
            self.data = Data.data_validation(self.data)

    @classmethod
    def convert(cls, user_data):
        """ Разделяет полученную строку на три переменные и проверяет на корректность ввода"""
        try:
            cls.day, cls.month, cls.year = [int(i.strip()) for i in user_data.split('-')]
        except ValueError:
            print('Недопустимые символы либо разделитель, необходимо указать дату в формате "01-01-2000"')
            return None
        else:
            return cls.day, cls.month, cls.year

    @staticmethod
    def data_validation(data):
        """Проверяет на корректность саму дату"""
        day, month, year = data
        if (1 > month) or (month > 12):
            print('Такого месяца не существует')
            return None

        if (-4000 > year) or (year > 4000):
            print('Такой год существует, но выглядит фантастично')
            return None

        if (month in [1, 3, 5, 7, 8, 10, 12]) and ((0 > day) or (day > 31)):
            print('Такого дня не существует')
            return None
        elif (month in [4, 6, 9, 11]) and ((0 > day) or (day > 30)):
            print('Такого дня не существует')
            return None

        if month == 2:
            if (year % 4 != 0) and (day > 28):
                print(f'В феврале {year} года нет такого дня')
                return None
            elif (year % 4 == 0) and (day > 29):
                print(f'В феврале {year} года нет такого дня')
                return None

        print(f"Дата {day:02}.{month:02}.{year} корректна")
        return 1


check = None
while check is None:
    a = Data(input('Введите дату в формате дд-мм-гггг : '))
    check = a.data

# _____________________ Задание 2 ()
print('Задание №2 ↓')


class ZeroDivisionPenalty(Exception):
    def __init__(self, txt):
        self.txt = txt


flag = True
while flag:
    try:
        a, b = int(input('Введите числитель : ')), int(input('Введите знаменатель : '))
        if b == 0:
            raise ZeroDivisionPenalty(f'Вот ты и попался, таинственный делитель на ноль!\nТеперь тебя вычислят по айпи'
                                      f' и выпишут {a}/0 часов\n'
                                      f'общественных работ в доме престарелых котов.')
        print(f'Результат деления {a} на {b} = {round(a / b, 2)}')
        flag = False
    except ValueError:
        print('Необходимо вводить только числа!')
    except ZeroDivisionPenalty as goodby:
        print(goodby)

#
# _____________________ Задание 3 ()
print('Задание №3 ↓')


class IsNotNumber(Exception):
    def __init__(self, text):
        self.text = text


user_li = []
count = 1
print('Программа составит список из введённых Вами чисел. ')
while True:
    try:
        el = input(f'Введите {count}-е число (или stop, чтобы завершить работу): ')
        if el.lower() == 'stop':
            print(f'Программа завершает работу.\nВаш список имеет следующий вид : \n'
                  f'{", ".join([str(i) for i in user_li])}')
            break
        if not el.replace('.', '').isdigit():
            raise IsNotNumber('Введённое значение не является числом')
        else:
            user_li.append(float(el))
            count += 1
    except IsNotNumber as err:
        print(err)

# _____________________ Задание 4-5-6 ()
print('Задание №4-5-6 ↓')


class Academy:
    """ Общие параметры академии"""
    _teachers = {"Пехота": "Джоно Баррати", "Флот": "Рагс Торго"}
    user_faculty = ''
    user_name = ''
    _faculty_lessons = {
        "Пехота": ["Тактика ведения боя в дифференцированных условиях экосистемы различных планет",
                   "Управление шагоходом AT-ST",
                   " Основы владения Е-11"],
        "Флот": ["Пилотирование и устройство TIE-Fighter",
                 "Манёвры и пилотирование в составе звена",
                 "Ориентирование в условиях открытого космоса"],
        "Рудники Кесселя": ["Добыча глиттерстима",
                            "Бегство от Энергетического паука",
                            "Стенания и страдания"]
    }
    __credits = 100

    @classmethod
    def faculty_choice(cls):
        """ Определяет в каком факультете будет учиться студент"""
        choice = 0
        choice += Academy.get_int('Ситуация 1: отряд штурмовиков попал в засаду на Фелуции и занял оборонительную '
                                  'позицию в остове корней большого дерева.\n Какой вариант спасения кажется Вам'
                                  ' наиболее рациональным?\n'
                                  '1 - С поддержкой дивизиона шагоходов AT-AS/AT-AT обеспечить проход к отряду'
                                  ' и организовать коридор отступления.\n'
                                  '2 - Использовать турболазеры Разрушителя для расчистки местности и, под прикрытием'
                                  ' группы TIE-истребителей, вывести отряд из окружения.\n'
                                  '3 - Не использовать шагоходы и ЗР, так как это может нанести серьёзный вред '
                                  'экосистеме планеты. Выслать новый отряд на помощь.\n'
                                  'Ваш выбор : ', 1, 3)
        choice += Academy.get_int('Ситуация 2: Повстанческий шпион выкрал важные документы в канцелярии гранд-моффа. '
                                  'Ему удалось сбежать и укрыться в небольшой прореспубликанской деревне\n на окраине '
                                  'космопорта. Жители деревни отказываются выдать шпиона имперскому патрулю.'
                                  'Как выйти из положения?\n'
                                  '1 - Предупредить жителей, что за неповиновение Империи они будут расстреляны. Начать'
                                  ' расстреливать по одному жителю, пока шпион не будет найден.\n'
                                  '2 - Вывести на орбиту Звёздный Разрушитель. Предупредить жителей, что в случае '
                                  'неповиновения вся деревня будет уничтожена вместе с похищенными данными.\n'
                                  '3 - Оба вышеуказанных метода излишне радикальны. Необходимо занять выжидательную'
                                  ' позицию, пока шпион не объявит себя.\n'
                                  'Ваш выбор : ', 1, 3)
        choice += Academy.get_int('Ситуация 3: губернатор системы Джабиим объявил о выходе из Империи и '
                                  'присоединении к гильдии рудокопов. Поставлена задача переубедить губернатора.\n'
                                  ' Каким образом это реализовать?\n'
                                  '1 - Направить небольшой отряд диверсантов в резиденцию губернатора. В удобный момент'
                                  ' убить губернатора и поставить на его место лояльного кандидата.\n'
                                  '2 - Заблокировать сектор, установить несколько ЗР класса "Воспрещающий", вести '
                                  'полную блокаду до тех пор, пока губернатор не примет верное решение.\n'
                                  '3 - Использовать экономические рычаги давления и политического влияния, для '
                                  'достижения необходимой цели.\n'
                                  'Ваш выбор : ', 1, 3)
        if choice in [3, 4, 5]:
            Academy.user_faculty = 'Пехота'
        elif choice in [6, 7, 8]:
            Academy.user_faculty = 'Флот'
        else:
            Academy.user_faculty = 'Рудники Кесселя'

    @staticmethod
    def get_string(text, base_value):
        """ Запрашивает у пользователя текстовое значение. В качестве аргументов принимает:
            text - запрос, который будет задан пользователю
            base_value - значение, которое будет установлено по умолчанию, если ничего не будет введено"""
        str_value = input(text)
        if str_value == '':
            str_value = base_value
        return str_value

    @staticmethod
    def get_int(text, start, end):
        """ Запрашивает у пользователя число и проверяет на допустимость. В качестве аргументов принимает :
            text - текст запроса
            start - начальное допустимое значение
            end - конечное допустимое значение"""
        text = text
        start = start
        end = end
        try:
            number = input(text)
            if number == '':
                return randint(start, end)
            else:
                number = int(number)
                if (number < start) or (number > end):
                    print('Введено число вне допустимых значений!')
                    return Academy.get_int(text, start, end)
                return number
        except ValueError:
            print('Необходимо ввести целое число!')
            return Academy.get_int(text, start, end)

    @property
    def credits(self):
        """ Показывает количество кредитов"""
        return self.__credits

    @credits.setter
    def credits(self, number):
        """ изменяет количество кредитов"""
        self.__credits = number


class Entertainment(Academy):
    """ Развлечения, соблазняющие курсантов во время обучения"""

    @property
    def pazaak_game(self):
        """ Упрощённый пазаак (он же 21-о очко). Кто первый перебрал 20-re, тот в пронусе. """
        answer = Academy.get_string(f'Ушлый курсант : "Эй, пс-с, друг, ты же с факультета {self.user_faculty}, да?'
                                    f' Наверное жутко скучно у вас там?\n'
                                    f'Ну не важно, давай-ка сыграем в карелианский пазаак! Я научу если не умеешь.'
                                    f' Ну как, да-нет? : ', 'да')
        if answer.lower() == 'да':
            answer_2 = Academy.get_string('Ха! Так держать! Ну тогда поехали, '
                                          'а.. а правила-то тебе рассказать? :', 'да')
            if answer_2.lower() == 'да':
                print('Да не переживай, тут всё просто, на - держи датапад для игры. Карелианский пазаак ещё проще '
                      'обычного.\n Каждый ход и мне и тебе выпадает карта, номиналом от 1 до 10 очков. И так ход за'
                      ' ходом.\nКто первый набрал больше 20-и, тот и проиграл. При том спассовать ты не можешь, '
                      'чистая удача! Играем до двух побед.')
            input("\033[32m {}\033[0m".format("press Enter"))
            bet = Academy.get_int('Лады, не будем тянуть вомпу-песчанку за хвост,'
                                  ' выбирай ставку до 50 кредитов и поехали: ', 1, 50)
            print("\033[33m {}\033[0m".format('____игра началась____'))
            main_score, second_score = 0, 0
            count_game = 1
            while (main_score != 2) and (second_score != 2):
                main_player, second_player = 0, 0
                print(f'Игра {count_game}-я, счёт {main_score}:{second_score}')
                while True:
                    a = randint(1, 10)
                    main_player += a
                    print(f'Ваша карта = {a}, сумма({main_player})')
                    if main_player > 20:
                        print('Вы проиграли раунд')
                        second_score += 1
                        sleep(2)
                        break
                    sleep(1)
                    a = randint(1, 10)
                    second_player += a
                    print(f'Карта соперника = {a}, сумма({second_player})')
                    if second_player > 20:
                        print('Соперник проиграл раунд')
                        main_score += 1
                        sleep(2)
                        break
                    sleep(2)
                count_game += 1
                print()
            if main_score > second_score:
                print('Ушлый курсант : "Эээх, ладно, ты выиграл, будь оно неладно, ну топай-топай отседова"')
                Academy.credits = self.credits + bet
            else:
                print('Ушлый курсант : "Хааа, вот она - моя удача. Ну не печалься, не печалься, гони кредиты!"')
                Academy.credits = self.credits - bet
        else:
            print('Ох, какой важный, играть не хочет. Ну и ... и пока тогда. *ботаник хренов*')

    @property
    def twilek_game(self):
        """ Вызывает отвязную тви-лечку, которая пытается кинуть персонажа на кредиты"""
        print("\033[33m {}\033[0m".format('____В коридорах академии Вы встретили симпатичную курсантку____'))
        answer = Academy.get_string(f'Курсантка тви-лекк : "Хэй, красавчик, тебя зовут {person.user_name}, верно?'
                                    f' Сегодня мы с подружками устраиваем вечеринку.\n'
                                    f'Приходи в гости, будет много сока джума, музыки и танцев, '
                                    f'будет весело! Придёшь?" да-нет? : ', 'да')
        input("\033[32m {}\033[0m".format("press Enter"))
        if answer == "да":
            a = randint(1, 49)
            Academy.credits = self.credits - a
            print(f"Вечеринка и вправду была умопомрачительная. Море выпивки, десяток не менее пьянящих курсанток\n"
                  f"и прохудившийся на {a} кредитов кошелёк.")
        else:
            print('Курсантка тви-лекк : "Ну как знаешь, прощай"')


class Faculty(Entertainment):
    """ Параметры факультета академии"""

    def __init__(self):
        self.lessons = Academy._faculty_lessons[Academy.user_faculty]
        self.rating = dict.fromkeys(self.lessons, 0)

    def get_knowledge(self, i):
        """ Играет с пользователем в простую угадайку. Разница между закаданным и угаданным числами
            идёт в зачёт дисциплины"""
        print(f'Обучение в Академии, четверть {i + 1}-я, дисциплина {self.lessons[i]}')
        rand_number = randint(1, 50)
        user_number = Academy.get_int('Введите Ваше число : ', 1, 50)
        print(f'Система загадала число {rand_number}, вы получаете {50 - abs(rand_number - user_number)} баллов '
              f'за дисциплину.')
        self.rating[self.lessons[i]] = 50 - abs(rand_number - user_number)


""" Создаём свою имперскую академию с пазааком и тви-лечками, принимаем курсанта и обрабатываем """

print('Давным-давно, в одной далёкой галактике.... ')
input("\033[32m {}\033[0m".format("press Enter"))
print('Ту-ту-ту-туууу-тууууу-ту-ту-ту-туууу-туууу (звуки Star Wars (c)tm)')
input("\033[32m {}\033[0m".format("press Enter"))
print(
    'Первая Галактическая Империя парсеками шагает по галактике, поглощая миры и навязывая свои суровые законы.\n'
    'Безжалостные жернова имперской машины перемалывают души миллионов новобранцев, решивших отдать свои жизни\n'
    'на служение Императору, в надежде выстроить безупречную карьеру в институте деспотичной тирании. ')
input("\033[32m {}\033[0m".format("press Enter"))
print(f'Вот и наш герой решил испытать удачу и вступить в ряды имперской Академии.')
input("\033[32m {}\033[0m".format("press Enter"))
print("\033[33m {}\033[0m".format('____Ваш герой улетел в Академию. Начинается игра от первого лица.____'))
input("\033[32m {}\033[0m".format("press Enter"))
Academy.user_name = Academy.get_string('Дроид-проводник : "О, новый курсант! Добро пожаловать в имперскую Академию. '
                                       'Здесь мы готовим лучших солдат для служения Императору.\n '
                                       'Для начала давай определимся с твоим именем" (введите имя) : ', 'Усат Котэ')
print('Дроид-проводник : "Отлично! Теперь нам нужно решить на какой факультет тебя определить.'
      ' Но сам ты выбрать не можешь, конечно.\n'
      'Я выберу факультет на основе результатов небольшого теста, в ходе которого будут выявлены твои навыки. Начнём?')
input("\033[32m {}\033[0m".format("press Enter"))
Academy.faculty_choice()
person = Faculty()

while person.user_faculty == 'Рудники Кесселя':
    print('Дроид-проводник : "Тревога!! Повстанческий шпион проник в Академию! Охрааанаааа...')
    input("\033[32m {}\033[0m".format("press Enter"))
    print(
        f'Результаты теста показали, что Вы - повстанческий шпион. Вас схватили и отправили на рудники Кесселя.\n'
        f' Однако, Вы не намерены провести остаток своих дней находясь в рабстве, бесконечно изучая дисциплины '
        f': \n {person.lessons} \nВы сбегаете с рудников, возвращаетесь в академию и снова проходите тест.')
    input("\033[32m {}\033[0m".format("press Enter"))
    Academy.faculty_choice()
    person = Faculty()

print(f'Дроид-проводник : "Превосходно! Основываясь на результатах тестирования тебе подойдёт факультет - \n'
      f'... 143@@%%#@@..$%$...Слизери*.. ОШИБКА"')
input("\033[32m {}\033[0m".format("press Enter"))
print(f'Дроид-проводник : "Ох, прошу прощения. Последнее время мой вокабулятор сбоит. '
      f'Так вот, твой факультет - {person.user_faculty}. '
      f'Твоим наставником будет {person._teachers[person.user_faculty]}"\n'
      f'Каждому студенту полагается 100 кредитов для личных нужд, вот, пожалуйста. А теперь располагайся в каюте'
      f' и начнём обучение.')
input("\033[32m {}\033[0m".format("press Enter"))
print("\033[33m {}\033[0m".format('____Ваш герой прибыл на первую лекцию.____'))
input("\033[32m {}\033[0m".format("press Enter"))

print(f'{person._teachers[person.user_faculty]} : "Курсанты! На моих курсах вы пройдёте '
      f'такие дисциплины как:\n{", ".join(person.lessons)}.\n'
      f'На каждом предмете вам будет необходимо набирать нужное количество баллов, чтобы пройти аттестацию'
      f' и получить профессию.\nЖелаю вам успехов и стра.. стараний. Кто не сдаст экзамен, поедет '
      f'на Татуин кормить Крайт-драконов.')
input("\033[32m {}\033[0m".format("press Enter"))
print("\033[33m {}\033[0m".format('____Ваш герой начал обучение.____'))
input("\033[32m {}\033[0m".format("press Enter"))
print('Учёба - долгая и сложная штука, поэтому для упрощения процесса Вам предлагается сыграть в игру.\n'
      'Система загадает число от 1 до 50, и Вам нужно это число отгадать. Чем дальше Ваше число будет от\n'
      'загаданного, тем меньше баллов вы получите за обучение. Мир жесток, как сам Император.')

for i in range(3):
    if i == 1:
        person.pazaak_game
    elif i == 2:
        person.twilek_game
    person.get_knowledge(i)
    input("\033[32m {}\033[0m".format("press Enter"))

print("\033[33m {}\033[0m".format('____Процесс обучения подходит к концу. Пришло время узнать кто на что учился.____'))
input("\033[32m {}\033[0m".format("press Enter"))
print(f'{person._teachers[person.user_faculty]} : "Курсанты! Наконец-то пришло время подводить итоги. Я очень надеюсь,'
      f'что мои старания не пошли банте под хвост,\nи хотя бы половина из вас набрала проходной балл 90 для успешного'
      f' выпуска из нашей академии. Ну что же, начнём.')
input("\033[32m {}\033[0m".format("press Enter"))
print(f'{person._teachers[person.user_faculty]} : {person.user_name}, подойди сюда')
input("\033[32m {}\033[0m".format("press Enter"))
print(f'{person._teachers[person.user_faculty]} : Так-таак, что тут у нас. Твои баллы по дисциплинам :\n'
      f'{person.rating}')
input("\033[32m {}\033[0m".format("press Enter"))
rate_sum = sum(person.rating.values())
credit_sum = person.credits
if rate_sum >= 90:
    print(f'{person._teachers[person.user_faculty]} : Молодец, курсант! За таких ребят меня всегда переполняет '
          f'гордостью. Империя воспитала достойного солтада!')
    input("\033[32m {}\033[0m".format("press Enter"))
    print("\033[33m {}\033[0m".format('____Вы успешно окончили академию. Теперь, получив должность в регулярной '
                                      'армии Империи, Вы сможете разжигать сердца триллионов жителей\n'
                                      '...взрывая их планеты.____'))
else:
    print(f'{person._teachers[person.user_faculty]} : Курсант... ты с горем-пополам набрал {rate_sum} баллов.'
          f' Но я видел твои старания. Так что...\n'
          f'Я бы смог компенсировать недостающие баллы равнозначным количеством кредитов в моём кармане ;-) ')
    input("\033[32m {}\033[0m".format("press Enter"))
    print("\033[33m {}\033[0m".format('____Вы судорожно полезли в кошелёк.____'))
    input("\033[32m {}\033[0m".format("press Enter"))
    print(f'У меня осталось {credit_sum} кредитов')
    input("\033[32m {}\033[0m".format("press Enter"))
    if credit_sum > (90 - rate_sum):
        print("\033[33m {}\033[0m".format('____Вы успешно окончили академию. Теперь, получив должность в регулярной '
                                          'армии Империи, Вы сможете разжигать сердца триллионов жителей галактики\n'
                                          '...взрывая их планеты.____'))
    else:
        print("\033[33m {}\033[0m".format('____Вы не смогли окончить академию. Как и было обещано, Вас отправили'
                                          'патрулировать безжизненные пустоши Татуина.____'))

# _____________________ Задание 7 ()
print('Задание №7 ↓')


class ComplexNumber:
    def __init__(self, num):
        try:
            if len(num) == 1 and num.isalpha():  # если ввели только i (0 + 1i)
                num = '0 + 1j'
            elif num[:-1].isnumeric() and num[-1].isalpha():  # если ввели только bi (0 + bi)
                num = '0 + ' + num
            if '+' in num:
                if num.replace(' ', '').index('+') == 0:  # если а + bi, где а == 0 и не пишется
                    num = '0' + num
                if len(num.replace(' ', '')[num.index('+'):-1]) == 0:  # если a + bi, где b == 1 и не пишется
                    num = num[:-1] + '1' + num[-1]
                self.n_num, self.mn_b_num = float(num[:num.index('+')]), float(num[num.index('+') + 1:-1])
            elif '-' in num:
                if num.replace(' ', '').index('-') == 0:  # если а - bi, где а == 0 и не пишется
                    num = '0' + num
                if len(num.replace(' ', '')[num.index('-'):-1]) == 1:  # если a - bi, где b == 1 и не пишется
                    num = num[:-1] + '1' + num[-1]
                self.n_num, self.mn_b_num = float(num[:num.index('-')]), float(num[num.index('-') + 1:-1]) * -1
            else:
                raise ValueError
            self.check = True
        except ValueError:
            print('Это число не комплексное')
            self.check = False

    def __add__(self, other):
        sign = ('+', '-')[(self.mn_b_num + other.mn_b_num) < 0]
        if (self.mn_b_num + other.mn_b_num) == 0:
            return f'{self.n_num + other.n_num}'
        else:
            return f'{self.n_num + other.n_num} {sign} {abs(self.mn_b_num + other.mn_b_num)}i'

    def __mul__(self, other):
        a = (self.n_num * other.n_num) + (self.mn_b_num * other.mn_b_num * -1)
        b = (self.n_num * other.mn_b_num) + (self.mn_b_num * other.n_num)
        sign = ('+', '-')[b < 0]
        if b == 0:
            return f'{a}'
        else:
            return f'{a} {sign} {abs(b)}i'


flag = True
while flag:
    a = ComplexNumber(input('Введите первое комплексное число : '))
    if a.check:
        while flag:
            b = ComplexNumber(input('введите второе комплексное число : '))
            if b.check:
                print(f'Результат сложения = {a + b}')
                print(f'Результат умножения = {a * b}\nПрограмма завершает работу')
                flag = False

            else:
                pass
    else:
        pass
