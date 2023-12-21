from turtle import *

speed(0)

def tp(x, y):
    penup()
    goto(x, y)
    pendown()


# тело
begin_fill()
circle(100, 390)
end_fill()

# грудка
color('gray')
left(90)
begin_fill()
circle(50, 125)
left(90)
circle(90, 60)
end_fill()

# глаз правый
tp(xcor() + 20, ycor() + 70)
begin_fill()
circle(30)
end_fill()

# глаз левый
tp(xcor() - 90, ycor())
begin_fill()
circle(30)
end_fill()

# зрачок левый
color('white')
tp(xcor(), ycor() + 15)
begin_fill()
circle(15)
end_fill()

color('black')
tp(xcor(), ycor() + 5)
begin_fill()
circle(7)
end_fill()

# зрачок правый

color('white')
tp(xcor() + 70, ycor() - 5)
begin_fill()
circle(15)
end_fill()

color('black')
tp(xcor() - 10, ycor() + 5)
begin_fill()
circle(7)
end_fill()

# клюв
tp(xcor() - 60, ycor() - 30)
color('orange')
seth(320)
begin_fill()
circle(50, 80)
end_fill()
seth(90)
begin_fill()
circle(30, 170)
end_fill()

# левая бровь
tp(xcor() - 50, ycor() + 70)
color('brown')
seth(330)
begin_fill()
for i in range(2):
    forward(60)
    left(90)
    forward(20)
    left(90)
end_fill()

# правая бровь
tp(xcor() + 130, ycor() + 20)
color('brown')
seth(210)
begin_fill()
for i in range(2):
    forward(60)
    left(90)
    forward(20)
    left(90)
end_fill()

# чубчик
tp(xcor() - 60, ycor() + 20)
seth(90)
color('black')
begin_fill()
circle(50, 50)
circle(10, 180)
circle(-50, 50)
end_fill()
circle(-50, -50)
color('brown')
begin_fill()
circle(10)
end_fill()

hideturtle()

exitonclick()
