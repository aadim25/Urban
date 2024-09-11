'''
Лекция. Практика. Часть 1. (Система регистрации на классах)
'''
class User:
    '''
    Класс пользователя, содержащий: логин, пароль
    '''
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

class Database:
    '''

    '''
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

if __name__ == '__main__':
    # Приведенный ниже комментарий относится к первой части
    # database = Database()
    # while True:
        # choice = input("Здравствуйте. Выберите пожалуйста действие:\n1-Вход\n2-Регистрация\n")
        # user = User(input('Введите логин: '),
        #             password := input('Введите пароль: '),
        #             password2 :=input('Подтвердите пароль: '))
        # if password != password2:
        #     exit()
        # database.add_user(user.username, user.password)
    database = Database()
    while True:
        choice = int(input("Здравствуйте. Выберите пожалуйста действие:\n1-Вход\n2-Регистрация\n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print (f"Вход выполнен, {login}")
                else:
                    print ("Неверный пароль")
            else:
                print ("Пользователь не найден.")
        if choice == 2:
            user = User(input('Введите логин: '),
                        password := input('Введите пароль: '),
                        password2 :=input('Подтвердите пароль: '))
            if (password != password2):
                print ("Пароли не совпадают, попробуйте ещё.")
                continue
            database.add_user(user.username, user.password)
        print (database.data)