from turtle import *

t = Turtle()
from time import sleep 

t.speed(100)

#faceis

#bandeira do japão

t.pu()
t.goto(-100, 0)
t.pd()

for _ in range(3):
        t.fd(500)
        t.lt(90)
        t.fd(300)
        t.lt(90)
t.end_fill()

t.pu()
t.goto(150, 200)
t.pd()
t.color("red")
t.begin_fill()
t.fillcolor("red")
t.circle(50)
t.end_fill()
sleep(5)
t.clear()


#polonia

t.pu()
t.goto(-250,125)
t.pd()
t.color("black")
t.right(180)
for _ in range(2):
        t.fd(500)
        t.rt(90)
        t.fd(150)
        t.rt(90)
t.end_fill
t.pu()
t.goto(-250,-25)
t.pd()
t.color("red")
t.begin_fill()
t.fillcolor("red")
for _ in range(2):  
         t.fd(500)
         t.right(90)
         t.fd(150)
         t.right(90)
t.end_fill()
sleep(5)
t.clear()

#media

#niger
t.pu()
t.goto(-250,125)
t.rt(180)
t.pd()
t.color("black")
t.right(180)
for _ in range(2):
        t.fd(500)
        t.rt(90)
        t.fd(300)
        t.rt(90)

mainloop()

