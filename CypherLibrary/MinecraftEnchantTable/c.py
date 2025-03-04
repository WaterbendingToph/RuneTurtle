import turtle
window = turtle.Screen()
window.setup(width = 200, height = 200)

length =        20
bottomLeft =    -50, -50
bottomRight =   50, -50
topLeft =       -50, 50
topRight =      50, 50

turtle.mode("logo")
turtle.pencolor("red")
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.setheading(90)
turtle.forward(200)
turtle.penup()
turtle.goto(-50, -100)
turtle.pendown()
turtle.setheading(0)
turtle.forward(200)
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.setheading(90)
turtle.forward(200)
turtle.penup()
turtle.goto(50, 100)
turtle.pendown()
turtle.setheading(180)
turtle.forward(200)

turtle.penup()
turtle.pencolor("blue")
turtle.goto(-50, -30)
turtle.pendown()
turtle.setheading(90)
turtle.forward(100)
turtle.penup()
turtle.goto(50, -10)
turtle.pendown()
turtle.setheading(270)
turtle.forward(100)
turtle.penup()
turtle.goto(-50, 10)
turtle.pendown()
turtle.setheading(90)
turtle.forward(100)
turtle.penup()
turtle.goto(50, 30)
turtle.pendown()
turtle.setheading(270)
turtle.forward(100)

turtle.penup()
turtle.goto(-30, 50)
turtle.pendown()
turtle.setheading(180)
turtle.forward(100)
turtle.penup()
turtle.goto(-10, -50)
turtle.pendown()
turtle.setheading(0)
turtle.forward(100)
turtle.penup()
turtle.goto(10, 50)
turtle.pendown()
turtle.setheading(180)
turtle.forward(100)
turtle.penup()
turtle.goto(30, -50)
turtle.pendown()
turtle.setheading(0)
turtle.forward(100)
turtle.penup()
turtle.pencolor("black")

#START
turtle.penup()
turtle.goto(topLeft)
turtle.setheading(90)
turtle.forward(length)
turtle.pendown()
turtle.begin_fill()
turtle.forward(length)
turtle.setheading(180)
turtle.forward(length)
turtle.setheading(270)
turtle.forward(length)
turtle.setheading(0)
turtle.forward(length)
turtle.end_fill()

turtle.penup()
turtle.setheading(180)
turtle.forward(length * 2)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(90)
turtle.forward(length)
turtle.setheading(180)
turtle.forward(length)
ReturnPoint = turtle.position()
turtle.setheading(270)
turtle.forward(length)
turtle.setheading(0)
turtle.forward(length)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(length)
turtle.setheading(180)
turtle.forward(length * 2)
turtle.setheading(270)
turtle.forward(length)
turtle.setheading(0)
turtle.forward(length * 2)
turtle.end_fill()
#END

turtle.done()