import turtle as tur,time,sys

tur.setup(width=600,height=350)

t=tur.Turtle()
t.fillcolor('#d500f9')
t.begin_fill()

tur.bgcolor('#131418')
t.speed(20)
t.pensize(10)
t.pencolor('white')
def p():
    t.penup()
    t.goto(-240,120)
    t.pendown()
    t.fd(12)
    t.circle(-20,180)
    t.fd(10)
    t.rt(90)
    t.fd(40)
    t.bk(80)
    t.penup()
    t.goto(-165,110)
p()



def a():
    t.pendown()
    t.lt(60)
    t.circle(20,120)
    t.fd(55)
    t.bk(60)
    t.lt(60)
    t.rt(250)
    t.circle(-20,170)
    t.fd(55)
    t.rt(180)
    t.fd(30)
    t.lt(90)
    t.fd(40)
    t.penup()
    t.goto(-120,110)
a()
def s():
    t.pendown()
    t.rt(90)
    t.circle(10,180)
    t.fd(10)
    t.lt(75)
    t.fd(60)
    t.rt(40)
    t.circle(-30,220)
    t.penup()
    t.goto(-65,110)

s()
def w():
    t.pendown()
    t.rt(170)
    t.fd(70)
    t.lt(160)
    t.fd(70)
    t.rt(150)
    t.fd(70)
    t.lt(150)
    t.fd(40)
    t.circle(60,140)
    t.penup()
    t.goto(10,90)
    t.penup()
    


   
w()
def o():
    t.pendown()
    t.circle(20,360)
    t.penup()
    t.goto(90,110)
o()

def r():
    t.pendown()
    t.rt(90)
    t.circle(20,145)
    t.fd(60)
    t.rt(180)
    t.fd(60)
    t.circle(-20,280)
    t.lt(130)
    t.fd(50)
    t.penup()
    t.goto(120,110)
   
r()

def d():
    t.pendown()
    t.rt(30)
    t.fd(70)
    t.rt(180)
    t.fd(60)
    t.circle(-15,200)
    t.fd(55)
    t.penup()
    t.goto(170,110)
d()

def i():
    t.pendown()
    t.lt(20)
    t.fd(60)
    t.penup()
    t.goto(200,110)
i()
def f():
    t.pendown()
    t.lt(95)
    t.rt(95)
    t.fd(60)
    t.rt(180)
    t.fd(50)
    t.circle(-15,180)
    t.rt(180)
    t.circle(15,180)
    t.fd(20)
    t.lt(90)
    t.fd(30)
    t.penup()
    t.goto(250,110)
f()

def y():
    t.pendown()
    t.rt(90)
    t.fd(20)
    t.circle(10,160)
    t.fd(20)
    t.bk(70)
    t.penup()
    t.goto(100,-25)
    t.write('software',font='tahoma,20')
    t.penup()
    t.goto(120,-70)
    t.write('version1.0',font=('vivaldi 30 normal'))

    t.end_fill()

y()

def welcome():
    time.sleep(3)

welcome()
