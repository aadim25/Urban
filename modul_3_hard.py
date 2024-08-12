'''Дополнительное практическое задание по модулю: "Подробнее о функциях."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности


Задание "Раз, два, три, четыре, пять .... Это не всё?":
Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются
в том, что намудрили вчера вечером.
Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые).
Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
1+2+3+1+4+1+5+6+4+7+4+8+5+2+5+6+35
Увидев это студент задался вопросом: "А есть ли универсальное решение для
подсчёта суммы всех чисел и длин всех строк?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.

Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения
для таких структур он не нашёл.

Помогите сокурснику осуществить его задумку.

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99


Примечания (рекомендации):
Весь подсчёт должен выполняться одним вызовом функции.
Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
Для определения типа данного используйте функцию isinstance.

Файл с кодом (module_3_hard.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий с файлом решения.'''
#print(1+2+3+1+4+1+5+6+4+7+4+8+5+2+5+6+35)
summa=0
def type_number(number):
    if type(number) == str:
        if len(number)==0:
            return 0
        return len(number)
    elif type(number) == (int or float):
        return number

def calculate_structure_sum(data_structure):
    global summa
    while not isinstance (data_structure, int | float | str):
        if type(data_structure) == list:
            for i in data_structure:
                calculate_structure_sum(i)
            return summa
        elif type(data_structure) == set:
            for i in (data_structure):
                calculate_structure_sum (i)
            return summa
        elif type(data_structure) == tuple:
            for i in data_structure:
                calculate_structure_sum(i)
            return summa
        elif type(data_structure) == dict:
            for key, value in data_structure.items():
                calculate_structure_sum(key)
                calculate_structure_sum(value)
            return summa
    else:
        summa += type_number (data_structure)
        return summa



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print (result)
