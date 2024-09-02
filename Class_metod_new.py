# print (int.__mro__)
# print(object)
class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print ('Я в нью')
        # return super().__new__(cls)
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, *args, **kwargs):
        print ("Я в ините")
        self.args = args
        for key, value in kwargs.items():
            setattr(self, key, value)
        # self.kwargs = kwargs
        # self.name = kwargs.get('name')
        # self.age = kwargs.get('age')

        


user1 = User()
# user2 = User()
# print (id(user1))
# print (id(user2))
print (User.__mro__)
# print (user1)
other = [1,2,3]
user = {'name': 'Ден', 'age': 25, 'gender':'male'}

user1 = User (*other, **user)
print (user1.args)
# print (user1.kwargs)
# print (user1.name)
# print (user1.age)

print (user1.args)
# print (user1.kwargs)
# print (user1.name)

print (int.__mro__ )
print(object)
# user1 = User (other,
#               user,
#               name = 'Den'
#               )
print (user1.args)
print (user1.name,
       user1.age,
       user1.gender)
# print (user1.kwargs)