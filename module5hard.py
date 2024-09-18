class User:
   def __init__(self, nickname, password, age):
        self.name = nickname
        self.position = password
        self.age = age

class Video:
    def __init__(self, title, duration,tine_now, audit_mode, bool):
        self.title = title
        self.duration = duration
        self.time_now = tine_now
        self.audit_mode = audit_mode
        self.bool = bool
    # def get_video(self,*args):
    #     return
    # def watch_video(self,*args):

class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    # def log_in(self, nickname, password):

    # def register(self, nickname, password, age):

    # def log_out(self):
    # def add(self,**kwargs):
