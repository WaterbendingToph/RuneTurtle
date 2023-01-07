import turtle
window = turtle.Screen()
window.setup(width = 360, height = 360)

length =        40
ReturnPoint =   0,0
direction = 1
topLeft =       -140, 140
if direction == 2:
    topLeft =   140, 140
if direction == 3:
    topLeft =   -140, -140
if direction == 4:
    topLeft =   140, 140
bottomLeft =    -140, -140
if direction == 2:
    bottomLeft = 140, -140
if direction == 3:
    bottomLeft = 140, -140
if direction == 4:
    bottomLeft = -140, 140

up = 0
if direction == 3:
    up = 270
if direction == 4:
    up = 90
right = 90
if direction == 2:
    right = 270
if direction == 3:
    right = 0
if direction == 4:
    right = 180
down = 180
if direction == 3:
    down = 90
if direction == 4:
    down = 270
left = 270
if direction == 2:
    left = 90
if direction == 3:
    left = 180
if direction == 4:
    left = 0

turtle.speed(0)

turtle.mode("logo")
turtle.pencolor("red")
turtle.penup()
turtle.goto(-140, -180)
turtle.setheading(0)
turtle.pendown()
turtle.forward(360)

turtle.penup()
turtle.goto(-180, 140)
turtle.pendown()
turtle.setheading(90)
turtle.forward(360)

turtle.penup()
turtle.goto(140, 180)
turtle.pendown()
turtle.setheading(180)
turtle.forward(360)

turtle.penup()
turtle.goto(180, -140)
turtle.pendown()
turtle.setheading(270)
turtle.forward(360)

turtle.pencolor("blue")
turtle.penup()
turtle.goto(-100, -140)
turtle.pendown()
turtle.setheading(0)
turtle.forward(280)

turtle.penup()
turtle.goto(-60, 140)
turtle.pendown()
turtle.setheading(180)
turtle.forward(280)

turtle.penup()
turtle.goto(-20, -140)
turtle.pendown()
turtle.setheading(0)
turtle.forward(280)

turtle.penup()
turtle.goto(20, 140)
turtle.pendown()
turtle.setheading(180)
turtle.forward(280)

turtle.penup()
turtle.goto(60, -140)
turtle.pendown()
turtle.setheading(0)
turtle.forward(280)

turtle.penup()
turtle.goto(100, 140)
turtle.pendown()
turtle.setheading(180)
turtle.forward(280)

turtle.penup()
turtle.goto(140, -100)
turtle.pendown()
turtle.setheading(270)
turtle.forward(280)

turtle.penup()
turtle.goto(-140, -60)
turtle.pendown()
turtle.setheading(90)
turtle.forward(280)

turtle.penup()
turtle.goto(140, -20)
turtle.pendown()
turtle.setheading(270)
turtle.forward(280)

turtle.penup()
turtle.goto(-140, 20)
turtle.pendown()
turtle.setheading(90)
turtle.forward(280)

turtle.penup()
turtle.goto(140, 60)
turtle.pendown()
turtle.setheading(270)
turtle.forward(280)

turtle.penup()
turtle.goto(-140, 100)
turtle.pendown()
turtle.setheading(90)
turtle.forward(280)

turtle.pencolor("black")

#START
turtle.penup()
turtle.goto(bottomLeft)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(up)
turtle.forward(length * 7)
turtle.setheading(right)
turtle.forward(length * 3)
turtle.setheading(down)
turtle.forward(length * 6)
turtle.setheading(right)
turtle.forward(length * 2)
turtle.setheading(down)
turtle.forward(length)
ReturnPoint = turtle.position()
turtle.setheading(left)
turtle.forward(length * 3)
turtle.setheading(up)
turtle.forward(length * 6)
turtle.setheading(left)
turtle.forward(length)
turtle.setheading(down)
turtle.forward(length * 6)
turtle.setheading(left)
turtle.forward(length)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint)
turtle.setheading(up)
turtle.forward(length * 6)
turtle.pendown()
turtle.begin_fill()
turtle.forward(length)
turtle.setheading(left)
turtle.forward(length)
turtle.setheading(down)
turtle.forward(length)
turtle.setheading(right)
turtle.forward(length)
turtle.end_fill()
#END

turtle.done()