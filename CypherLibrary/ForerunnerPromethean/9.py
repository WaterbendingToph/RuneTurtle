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
endPointX = initialX - lineWidth
while turtle.xcor() > endPointX:
    turtle.forward(1)
verticalOffset = turtle.ycor() - initialY
turtle.setheading(0)
turtle.forward(letterHeight - lineWidth * (3/2) - verticalOffset * 2)
ReturnPoint = turtle.position()
tempVar = initialX
initialX = endPointX
endPointX = tempVar
turtle.setheading(60)
while turtle.xcor() < endPointX:
    turtle.forward(1)
turtle.setheading(180)
turtle.forward(letterHeight - lineWidth * 3/2)
turtle.end_fill()

turtle.penup()
turtle.backward(letterHeight - lineWidth)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(240)
lineStart = turtle.position()
initialX = turtle.xcor()
endPointX = initialX - 2 * lineWidth
while turtle.xcor() > endPointX:
    turtle.forward(1)
lineLength = turtle.distance(lineStart)
turtle.setheading(0)
turtle.forward(lineWidth)
turtle.setheading(60)
turtle.forward(lineLength)
turtle.setheading(120)
turtle.forward(lineLength / 2)
rightWall = turtle.xcor()
turtle.setheading(180)
turtle.forward(lineWidth)
turtle.setheading(300)
turtle.forward(lineLength / 2)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint)
turtle.setheading(180)
turtle.forward(lineWidth * 2)
turtle.setheading(270)
turtle.forward(lineWidth / 2)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(180)
turtle.forward(lineWidth)
turtle.setheading(240)
turtle.forward(lineLength / 2)
turtle.setheading(0)
turtle.forward(lineWidth)
turtle.setheading(60)
turtle.forward(lineLength / 2)
turtle.end_fill()
#END

turtle.done()