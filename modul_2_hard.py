'''
Дополнительное практическое задание по модулю: "Основные операторы"

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

Задание "Слишком древний шифр":
Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени
(да-да, классика "Индиана Джонса").
К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.
В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.

К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны правила для
решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).

Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка)
сумме их значений.

Пример кратности(деления без остатка):
1 + 2 = 3 (сумма пары)
9 / 3 = 3 (ровно 3 без остатка)
9 кратно 3 (9 делится на 3 без остатка)

'''

import random
def chek_digit (number):
    my_list = []
    for i in range(2, int(number)):
        for j in range(2,i):
            if number % (i + j) == 0:
                my_list.append((i,j))
    return my_list

number1 = random.randint(3,20)
print(number1)
print(chek_digit(number1))