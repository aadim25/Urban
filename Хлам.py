def text_func (*param):
    print ("Тип:", type(param))
    print ("Аргумент", *param)

def summator (txt, *value):
    s = 0
    for i in value:
        s +=1
    return f'{txt}{s}'


# text_func(1,2,3,4)
print (summator ('Сумма чисел:',2,3,5))