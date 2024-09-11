'''
Повторение материала по вебинару
https://kinescope.io/jQDkXv6qxp5CEb8x7VHy9r
от 29-07-24.
Рассмотрены вопросы по работе с переменными разной области видимости
'''
global_var = 'global'
def local_function(global_arg):
    global global_var
    local_var = 'local'
    global_var = 'global change'
    # print (local_var)
    # print (global_var)
    print (locals())

local_function('local_arg')
print (globals())

count = 10
def outer_function(arg):
    enclosing_var = 'enclosing'
    count = 20
    # print (locals())
    print ('Счетчик объемлющего пространства имен', count)
    def inner():
        print(locals())
        count = 30
        print (enclosing_var)
        print('Счетчик локального пространства имен', count)

    inner()

outer_function('123456')
print('Счетчик глобального пространства имен', count)

def outer_function():
    count = 10
    def plus_count():
        nonlocal count
        count +=1
        print(count)
    return plus_count

plus = outer_function()
for i in range(10):
    plus()

abcde = 10
def outer_func():
    abcd = 20
    def inner_func():
        abc = 30

tasks = []

def add(task):
    # локальное пространство имен: task
    print ("Добавление задачи", task)
    tasks.append(task)

def remove_task(index):
    # локальное пространство имён: index
    if 0 <= index < len (tasks):
        tasks.pop(index)
    else:
        print ("Ошибка индекса")

def filter_tasks(keyword):
    def filter_functiom(task):
        if keyword in task:
            return True
        else:
            return False

    filtered_task = list(filter(filter_function, tasks))
    return filtered_task

if __name__ == '__main__':
    add('Купить молоко')
    add('Выучить переменные в Python')
    add('Функции в Python')
    print (filter_tasks('Python'))

# add('Купить молоко')
# print (tasks)
