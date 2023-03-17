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
turtle.setheading(30)
turtle.forward(lineWidth)
turtle.setheading(90)
turtle.forward(lineWidth * 2)
ReturnPoint = turtle.position()
turtle.setheading(150)
turtle.forward(lineWidth * 3)
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.setheading(330)
turtle.forward(lineWidth * 2)
turtle.setheading(270)
turtle.forward(lineWidth * 2)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint)
turtle.setheading(90)
turtle.forward(lineWidth / 2)
turtle.pendown()
turtle.begin_fill()
turtle.forward(lineWidth)
turtle.setheading(150)
turtle.forward(lineWidth * 3)
ReturnPoint = turtle.position()
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.setheading(330)
turtle.forward(lineWidth * 3)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint)
turtle.setheading(90)
turtle.forward(lineWidth / 2)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(30)
turtle.forward(lineWidth * 2)
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.setheading(210)
turtle.forward(lineWidth)
turtle.setheading(150)
turtle.forward(lineWidth)
turtle.end_fill()

turtle.penup()
turtle.setheading(30)
turtle.forward(lineWidth * 4)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(270)
turtle.forward(lineWidth * 6)
turtle.setheading(330)
turtle.forward(lineWidth)
turtle.setheading(30)
turtle.forward(lineWidth)
turtle.setheading(270)
turtle.forward(lineWidth / 2)
turtle.setheading(30)
turtle.forward(lineWidth)
turtle.setheading(90)
turtle.forward(lineWidth * 0.5)
turtle.setheading(150)
turtle.forward(lineWidth)
turtle.setheading(210)
turtle.forward(lineWidth)
turtle.setheading(90)
turtle.forward(lineWidth * 5)
turtle.setheading(30)
turtle.forward(lineWidth)
turtle.setheading(270)
turtle.forward(lineWidth * 3)
turtle.setheading(30)
turtle.forward(lineWidth)
turtle.setheading(90)
turtle.forward(lineWidth * 3)
turtle.setheading(150)
turtle.forward(lineWidth)
rightWall = turtle.xcor()
turtle.setheading(210)
turtle.forward(lineWidth * 2)
turtle.end_fill()
#END

turtle.done()