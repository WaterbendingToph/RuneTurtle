import turtle
window = turtle.Screen()
window.setup(width = 600, height=600)

letterHeight = 400
lineWidth = 20
rightWall = 0
initialX = 0
initialY = 0
endPointX = 0
endPointY = 0
verticalOffset = 0
horizontalOffset = 0

turtle.mode("logo")
turtle.penup()
turtle.pencolor("red")
turtle.goto(-300, -250)
turtle.pendown()
turtle.setheading(90)
turtle.forward(600)
turtle.penup()
turtle.goto(250, -300)
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.penup()
turtle.goto(300, 250)
turtle.pendown()
turtle.setheading(270)
turtle.forward(600)
turtle.penup()
turtle.goto(-250, 300)
turtle.pendown()
turtle.setheading(180)
turtle.forward(600)
turtle.penup()
turtle.pencolor("blacK")

turtle.goto(-lineWidth / 2, -letterHeight / 2)
turtle.pendown()


#START
turtle.begin_fill()
turtle.setheading(300)
initialX = turtle.xcor()
initialY = turtle.ycor()
endPointX = turtle.xcor() - lineWidth * 2
while turtle.xcor() > endPointX:
    turtle.forward(1)
turtle.setheading(0)
turtle.forward(lineWidth * 2)
turtle.setheading(60)
endPointX = turtle.xcor() + lineWidth
while turtle.xcor() < endPointX:
    turtle.forward(1)
turtle.setheading(180)
turtle.forward(lineWidth * 2)
ReturnPoint = turtle.position()
turtle.setheading(120)
while turtle.xcor() < initialX:
    turtle.forward(1)
turtle.setheading(180)
while turtle.ycor() > initialY:
    turtle.forward(1)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint)
turtle.setheading(45)
turtle.forward(lineWidth / 2)
turtle.pendown()
turtle.begin_fill()
initialY = turtle.ycor()
turtle.setheading(120)
endPointX = turtle.xcor() + lineWidth
while turtle.xcor() < endPointX:
    turtle.forward(1)
turtle.setheading(0)
turtle.forward(letterHeight - lineWidth * 3)
turtle.setheading(240)
endPointX = turtle.xcor() - lineWidth
while turtle.xcor() > endPointX:
    turtle.forward(1)
ReturnPoint = turtle.position()
turtle.setheading(180)
turtle.forward(turtle.ycor() - initialY)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint)
turtle.setheading(240)
turtle.forward(lineWidth / 2)
turtle.setheading(180)
turtle.forward(lineWidth)
turtle.pendown()
turtle.begin_fill()
turtle.forward(lineWidth)
turtle.setheading(240)
turtle.forward(lineWidth)
turtle.setheading(0)
turtle.forward(lineWidth)
turtle.setheading(60)
turtle.forward(lineWidth)
turtle.end_fill()
#END

turtle.done()