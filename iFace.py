from turtle import *

tInt = Turtle()
tInt.speed(-1)
tInt.ht()

def palitr(x, y, col, simvol):
    tInt.penup()
    tInt.goto(x,y)
    tInt.color(col)
    tInt.pendown()
    tInt.begin_fill()
    for t in range(4):
        tInt.forward(20)
        tInt.left(90)
    tInt.end_fill()
    tInt.penup()
    tInt.goto(x+5,y-20)
    tInt.color("black")
    tInt.write(simvol, font = ("Arial", 12, "normal"))

def zal(x,y):
    tInt.penup()
    tInt.goto(x,y)
    tInt.pendown()
    tInt.write("Заливка: начало - z, конец - x", font = ("Arial", 10, "normal"))

def line(x,y, wid, simvol):
    tInt.penup()
    tInt.goto(x,y)
    tInt.pendown()
    tInt.width(wid)
    tInt.color("grey")
    tInt.setheading(90)
    tInt.forward(10)
    tInt.penup()
    tInt.goto(x+10,y)
    tInt.pendown()
    tInt.write(simvol, font = ("Arial", 12, "normal"))

palitr(100,150, "silver", "a")
palitr(140,150, "seagreen", "w")
palitr(180,150, "mediumorchid", "d")
palitr(220,150, "blue", "s")
zal(-140, 150)
line(-200, 150, 5, "1")
line(-200, 110, 10, "2")
line(-200, 70, 15, "3")