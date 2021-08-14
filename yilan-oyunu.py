import random
from tkinter import font
from tkinter.constants import CENTER
import turtle
import time
delay=0.15
pencere=turtle.Screen()
pencere.title=("Yazamayanlar Snake Game")
pencere.bgcolor('lightgreen')
pencere.setup(width=600, height=600)
pencere.tracer(0)
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,100)
head.direction="stop"

yemek=turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()
yemek.shapesize(0.80,0.80)
yemek.goto(0,0)

kuyruklar=[]
puan=0

yaz=turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("white")
yaz.penup()
yaz.hideturtle()
yaz.goto(0,260)
yaz.write("Puan : {}".format(puan),align="center",font=("Courier",24,"normal"))
def move():
    if (head.direction == "up") :
        y=head.ycor()
        head.sety(y+20)
    if  (head.direction == "down") :
        y=head.ycor()
        head.sety(y-20)
    if  (head.direction == "right") :
        x=head.xcor()
        head.setx(x+20)
    if  (head.direction == "left") :
        x=head.xcor()
        head.setx(x-20)
def go_up():
    if head.direction !="down":
        head.direction ="up"
def go_down():
    if head.direction !="up":
       head.direction ="down"

def go_left():
    if head.direction !="right":
        head.direction ="left"

def go_right():
    if head.direction !="left":
       head.direction ="right"


pencere.listen()
pencere.onkey(go_up,"Up")
pencere.onkey(go_down,"Down")
pencere.onkey(go_right,"Right")
pencere.onkey(go_left,"Left")
while True:
    pencere.update()
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() <-300:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for kuyruk in kuyruklar:
            kuyruk.goto(1000,1000)
            kuyruklar=[]
        puan=0
        delay=0.1
        yaz.clear()
        yaz.write("Puan : {}".format(puan), align="center",font=("Courier",24,"normal"))
    if head.distance(yemek)<20:
        x= random.randint(-250,250)
        y= random.randint(-250,250)
        yemek.goto(x,y)
        yeni_kuyruk =turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("white")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)
        delay -=0.001
        puan=puan+10
        yaz.clear()
        yaz.write("Puan : {}".format(puan), align="center",font=("Courier",24,"normal"))
    for index in range(len(kuyruklar)-1,0,-1):
        x=kuyruklar[index-1].xcor()
        y=kuyruklar[index-1].ycor()
        kuyruklar[index].goto(x,y)
    if len(kuyruklar)>0:
        x=head.xcor()
        y=head.ycor()
        kuyruklar[0].goto(x,y)
    move()
    for segment in kuyruklar:
        if segment.distance(head)<20:
            time.sleep()
            head.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000,1000)
            kuyruklar=[1]
            puan=0
            yaz.clear()
            yaz.write("Puan : {}".format(puan), align="center",font=("Courier",24,"normal"))
            hiz=0.15
    time.sleep(delay)
