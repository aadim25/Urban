from .module1 import hello
from dis import dis

def say_hi():
    print ("Я из функции во втором модуле")

def main():
    a = 5
    b = 10
    print("Привет")

def some_func():
    a = "Я из второго модуля"
    print("Я из второго модуля")
    return a

# dis(some_func)
# print ("Вызов модуля 2 в модуль 3")
def goodword(name):
    hello(name)
    print ('Ты лучший', name)

if __name__ =='__main__':
    goodword('Урбан')