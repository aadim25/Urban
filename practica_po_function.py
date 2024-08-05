'''Практика по функциям
На сегодняшнем занятии мы проведём небольшую практику, посвящённую функциям. Нашей задачей будет написать три функции:
Первая - максимум в списке, то есть функцию, которая будет находить максимальный элемент в списке;
Вторая будет считать количество чётных чисел в переданном списке;
Третья функция будет возвращать нам уникальный список.
'''
def find_max (list_):
    max = list_[0]
    for i in list_:
        if max < i:
            max = i
    return max

def find_min (list_):
    min = list_[0]
    for i in list_:
        if min > i:
            min = i
    return min

def unique (list_):
    new_list = list()
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list

print (find_max ([1,2,2,45,78]))
print (find_min ([1,2,2,45,78]))
print (unique ([1,2,2,45,78,1,2,2,45,78]))