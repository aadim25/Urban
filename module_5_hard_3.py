class User:
    def __init__(self, nickname, password, age):
        print('init user')
        self.name = nickname
        self.password = hash(password)
        self.age = age
    
            
class Video:
    def __init__(self, title, duration,time_now, audit_mode, bool):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.audit_mode = audit_mode
        self.bool = bool
        
    def get_video(self,*args):
        pass


class UrTube:
    def __init__(self):
        print('init urtube')
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if self.user.nickname == nickname:
              print ('entry')
              
    def register(self, nickname, password, age):
        print(self.users)
        if User(nickname, password, age) in self.users:
            print('user')
        else:
            print('empty')
            new_user =  User(nickname, password, age)
            print('new')
            self.users.append(new_user)
            self.current_user = new_user
        
        
        
        
        
        
        
        
        
        
     
            
    def log_out(self):
        pass
    def add(self, **kwargs):
        pass

first_ut = UrTube()
first_ut.register('aadim', '578', 17)
#first_ut.log_in('aadim', '578')
first_ut.register('aadim', '578', 17)

#first_ut.log_in('aadim', '1234')
print(first_ut.users)