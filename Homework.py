from abc import ABC, abstractmethod

# ______________________ Задание 1 (Матрицы)
print('Задание №1 ↓')


class Matrix:
    def __init__(self, li=None):
        if li is None:
            self.li = Matrix.get_user_matrix()
        else:
            self.li = li

    def __str__(self):
        matrix_lenth = len(self.li)
        matrix_width = len(self.li[0])
        for i in range(matrix_lenth):
            print('_' * (matrix_width * 4 + 1))
            for j in range(matrix_width):
                if j == 0:
                    print('|', end='')
                print(str(self.li[i][j]).rjust(3), end='')
                print('|', end='')
            print()
        print('¯' * (matrix_width * 4 + 1))
        return f'Ваша матрица имеет размерность {matrix_lenth}x{matrix_width} ↑'

    def __add__(self, other):
        li_temp = []
        matrix_lenth = len(self.li)
        matrix_width = len(self.li[0])
        if matrix_width != len(other.li[0]) or matrix_lenth != len(other.li):
            decision_2 = input('Сложение матриц разных размерностей доступно в платной версии программы.\n'
                               'Желаете приобрести? (да/нет) : ')
            if decision_2.lower() == 'да':
                print('К этому я был не готов')
            return self.li
        for i in range(matrix_lenth):
            row_temp = []
            for j in range(matrix_width):
                row_temp.append(self.li[i][j] + other.li[i][j])
            li_temp.append(row_temp)
        return li_temp

    @staticmethod
    def get_user_matrix():
        """ Запрашивает у пользователя данные для формирования матрицы. Проверяет на корректность."""
        try:
            y = int(input('Введите количество строк в матрице : '))
            x = int(input('Введите количество столбцов в матрице : '))
            matrix = []

            def get_matrix_row(i, x):
                """ Запрашивает и проверяет строку матрицы в формате (1 3 4 5)"""
                i, x = i, x
                try:
                    row = [int(j) for j in input(f'Введите {i + 1}-ю строку : ').split()]
                    if len(row) != x:
                        print(f'Строка Вашей матрицы должна состоять из {x} {Matrix.get_ending(x, "число")}!')
                        return get_matrix_row(i, x)
                    else:
                        return row
                except ValueError:
                    print('Необходимо водить только числа!')
                    return get_matrix_row(i, x)

            print(f"Теперь введите по очереди {y} {Matrix.get_ending(x, 'строка')} матрицы из {x}"
                  f" {Matrix.get_ending(x, 'число')} через пробел "
                  f"({' '.join([str(i) for i in range(1, x + 1) if (i < 10) or (i == x)])})ect.")
            for i in range(y):
                matrix.append(get_matrix_row(i, x))
            return matrix
        except ValueError:
            print('Необходимо вводить только число!')
            return Matrix.get_user_matrix()

    @staticmethod
    def get_ending(end, word):
        if end in [11, 12, 13, 14]:
            if word == 'строка':
                return 'строк'
            else:
                return 'чисел'
        elif end % 10 in [1]:
            if word == 'строка':
                return 'строка'
            else:
                return 'числа'
        elif end % 10 in [2, 3, 4]:
            if word == 'строка':
                return 'строки'
            else:
                return 'чисел'
        else:
            if word == 'строка':
                return 'строк'
            else:
                return 'чисел'


decision = (False, True)[input('Хотите выполнить сложение двух матриц? (да/ нет) : ').lower() == 'да']
while decision:
    a = Matrix()
    b = Matrix()
    c = Matrix(a + b)
    print(c)
    decision = (False, True)[input('Желаете повторить? (да/ нет) : ').lower() == 'да']
print('Программа завершает работу\n\n')

# _____________________ Задание 2 (Расход ткани)
print('Задание №2 ↓')


class Clothes(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calc_cloth(self):
        """ Рассчитывает объём ткани, необходимый для пошива """
        pass

    def __add__(self, other):
        return self.calc_cloth + other.calc_cloth


class Coat(Clothes):

    def __init__(self, size):
        self.a = size

    @property
    def calc_cloth(self):
        return round(self.a / 6.5 + 0.5, 2)


class Suit(Clothes):

    def __init__(self, height):
        self.a = height

    @property
    def calc_cloth(self):
        return round((self.a / 100) * 2 + 0.3, 2)


def get_input(arg):
    """ Запришивает и проверяет значения размера/ роста для пошива пальто/ костюма"""
    arg = arg
    try:
        if arg == "пальто":
            user_input = int(input('Введите размер пальто (5 - 150) : '))
            if 0 < user_input < 5:
                print('Пошив пальто для младенцев запрещён международной конвенцией ООН по логике,'
                      ' будет установлен минимально допустимый размер')
                user_input = 5
            elif 250 > user_input > 150:
                print('К сожалению, пошив пальто таких размеров недоступен на нашей фабрике,'
                      'будет установлен максимально допустимый размер')
                user_input = 150
            elif user_input == 0:
                print('Не хочется шить пальто? А придётся! Иначе компартия заберёт твой кошкажена, комрад!'
                      'Будет установлен минимально допустимый размер')
                user_input = 5
            elif user_input < 0:
                print('Производство отрицательного размера пальто приведёт к аннигиляции материи и схлопыванию'
                      ' вселенной.\n Не будем форсировать события. Будет установлен минимально допустимый размер')
                user_input = 5
            elif user_input > 250:
                print('Великаны с планеты HIP 13044 b благодарны за внимание и заботу, но мы не будем шить '
                      'для них пальто. ')
                user_input = 150
        else:
            user_input = int(input('Введите рост для пошива костюма (80 - 210) : '))
            if 0 < user_input < 80:
                print('Пошив костюма для котов запрещён международной конвенцией ООН по защите животных,'
                      ' будет установлен минимально допустимый рост')
                user_input = 80
            elif 250 > user_input > 210:
                print('К сожалению, пошив костюма для баскетболистов недоступен на нашей фабрике,'
                      'будет установлен максимально допустимый рост')
                user_input = 210
            elif user_input == 0:
                print('Не хочется шить костюм? А придётся! Иначе в театре Вы будете белой вороной!'
                      'Будет установлен минимально допустимый размер')
                user_input = 80
            elif user_input < 0:
                print('Производство отрицательного размера костюма приведёт к отрицательному росту вашего кошелька.'
                      '\n Не будем нагнетать. Будет установлен минимально допустимый размер')
                user_input = 80
            elif user_input > 250:
                print('Великаны с планеты HIP 13044 b благодарны за внимание и заботу, но мы не будем шить '
                      'для них костюм. ')
                user_input = 210
        return user_input
    except ValueError:
        print('Необходимо ввести целое число!')
        return get_input(arg)


a = Coat(get_input('пальто'))
b = Suit(get_input('костюм'))
print(f'Расход ткани на пошив пальто =  {a.calc_cloth}')
print(f'Расход ткани на пошив костюма = {b.calc_cloth}')
print(f'Суммарный расход ткани = {a + b}')

# _____________________ Задание 3 ()
print('Задание №3 ↓')


class OrganicCell:
    def __init__(self, count=None):
        if count is None:
            self.cell_count = OrganicCell.get_cell_count()
        else:
            self.cell_count = count

    @staticmethod
    def get_cell_count():
        """ Запрашивает у пользователя количество ячеек клетки и проверяет на корректность """
        try:
            user_data = int(input('Введите количество ячеек в клетке : '))
            if user_data < 1:
                print('Количество ячеек не должно быть равно или меньше 0')
                return OrganicCell.get_cell_count()
            return user_data
        except ValueError:
            print('Необходимо ввести целое число!')
            return OrganicCell.get_cell_count()

    @staticmethod
    def get_group_count():
        try:
            user_group_count = int(input('Введите количество ячеек в одной группе : '))
            if user_group_count < 1:
                raise ValueError
            return user_group_count
        except ValueError:
            print('Необходимо ввести целое положительное число, отличное от 0')
            return OrganicCell.get_group_count()

    def __add__(self, other):
        return self.cell_count + other.cell_count

    def __sub__(self, other):
        if self.cell_count - other.cell_count > 0:
            return self.cell_count - other.cell_count
        elif self.cell_count - other.cell_count == 0:
            print('После вычитания получился ноль. Допустим, что одна ячейка чудом выжила, значение установлено на "1"')
            return 1
        else:
            print('Получилось отрицательное число. Допустим, что ячейки старой клетки подрались с новыми и'
                  ' остались выжившие из новых')
            return abs(self.cell_count - other.cell_count)

    def __mul__(self, other):
        return self.cell_count * other.cell_count

    def __truediv__(self, other):
        return round(self.cell_count / other.cell_count)

    def make_order(self, num):
        """ Возвращает строку с группами ячеек, разделёнными \n.
            В качестве аргумента принимает количество ячеек в группе"""
        str_temp = ''
        for i in range(self.cell_count // num):
            str_temp += '*' * num + '\n'
        return str_temp + '*' * (self.cell_count % num)


print('Программа запросит у вас количество ячеек исходной клетки и устроит битву'
      ' со сложением/вычитанием/умножением/делением.\n'
      'Для начала введите количество ячеек исходной клетки.')
a = OrganicCell()
print('Да начнётся битва! Сначала сложим базовые ячейки с новыми')
b = OrganicCell()
a = OrganicCell(a + b)
print(f'Результат сложения = {a.cell_count}. Теперь вычтем')
b = OrganicCell()
a = OrganicCell(a - b)
print(f'Результат вычитания = {a.cell_count}. Теперь умножим')
b = OrganicCell()
a = OrganicCell(a * b)
print(f'Результат умножения = {a.cell_count}. Теперь поделим')
b = OrganicCell()
a = OrganicCell(a / b)
print(f'Результат деления = {a.cell_count}.')

print(f'Визуализация распределения ячеек итоговой клетки: \n'
      f'{a.make_order(OrganicCell.get_group_count())}')
