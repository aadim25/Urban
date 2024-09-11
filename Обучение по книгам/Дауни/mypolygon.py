import turtle
# bob = turtle.Turtle()
# print(bob)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)
# turtle.mainloop()

def square(t,bob):
    for i in range(4):
        bob.fd(t)
        bob.lt(90)
    turtle.mainloop()

# square(165,bob)

def polygon(t,bob,n):
    alfa = 360/n
    for i in range(n):
        bob.fd(t)
        bob.lt(alfa)
    # turtle.mainloop()

my_bob = turtle.Turtle()
n = 9
step = 150
def circle (t,r,poly):
    
for i in range(3,n):
    polygon(step,my_bob,i)