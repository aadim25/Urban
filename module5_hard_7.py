'''
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!') '''

from time import sleep
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    
            
class Video:
    def __init__(self, title, duration,time_now, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                #print('Пользователь найден: ', user.nickname)
                self.current_user = user
                return
              
    def register(self, nickname, password, age):
        my_user = []
        for su in self.users:
            my_user.append(su.nickname)
        if nickname in my_user:
            print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.log_in(nickname, password)
        return


    def log_out(self):
        self.current_user = None

    def add(self, *args):
        add_list =[]
        for video in self.videos:
            add_list.append(video.title)
        for video in args:
            if video.title not in add_list:
                self.videos.append(video)

    def get_videos(self, word):
        video_lst = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                video_lst.append(video.title)
                #print(video_lst)
        return video_lst

    def watch_video(self, video):
        if self.current_user == None:
            print ('Войдите в аккаунт, чтобы смотреть видео')
            return
        else:
            for vd in self.videos:
                if vd.title == video:
                    if (vd.adult_mode and self.current_user.age < 18):
                        print ("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return
                    elif (vd.adult_mode and self.current_user.age >= 18) or (not vd.adult_mode and self.current_user.age < 18):
                        for my_time in range(1, vd.duration+1):
                            print (my_time, end = " ")
                            sleep(1)
                        print ("Конец видео")




ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200, 60)
v2 = Video('Для чего девушкам парень программист?', 10, 60, adult_mode = True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')