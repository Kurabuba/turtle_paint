from turtle import *
from iFace import *


# рисование
def draw(x,y):
    turtle1.goto(x,y)

def move(x,y):
    turtle1.penup()
    turtle1.goto(x,y)
    turtle1.pendown()

# клавиши
def up():
    turtle1.goto(turtle1.xcor(), turtle1.ycor() + 5)

def down():
    turtle1.goto(turtle1.xcor(), turtle1.ycor() - 5)

def left():
    turtle1.goto(turtle1.xcor() - 5, turtle1.ycor())

def right():
    turtle1.goto(turtle1.xcor() + 5, turtle1.ycor())

# цвета
def col():
    turtle1.color("silver")

def col1():
    turtle1.color("seagreen")

def col2():
    turtle1.color("mediumorchid")

def col3():
    turtle1.color("blue")

#ширина
def setWidth_1():
    turtle1.width(5)

def setWidth_2():
    turtle1.width(10)

def setWidth_3():
    turtle1.width(15)


# создание черепашки
turtle1 = Turtle()
turtle1.color("blue")
turtle1.shape("circle")
turtle1.width(10)
turtle1.speed(-1)

turtle1.ondrag(draw)

# объект с черепашкой
screen = turtle1.getscreen()
screen.onscreenclick(move)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
# смена цветов
screen.onkey(col, "a")
screen.onkey(col1, "w")
screen.onkey(col2, "d")
screen.onkey(col3, "s")
#заливка
screen.onkey(turtle1.begin_fill,"z")
screen.onkey(turtle1.end_fill,"x")
#ширина
screen.onkey(setWidth_1, "1")
screen.onkey(setWidth_2, "2")
screen.onkey(setWidth_3, "3")

exitonclick()