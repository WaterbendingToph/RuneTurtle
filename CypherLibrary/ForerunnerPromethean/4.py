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

turtle.goto(- 5 * lineWidth / 2, letterHeight * (-1/3) )
turtle.pendown()


#START
turtle.begin_fill()
turtle.setheading(120)
turtle.forward(lineWidth)
ReturnPoint = turtle.position()
turtle.setheading(0)
turtle.forward(lineWidth)
turtle.setheading(300)
turtle.forward(lineWidth)
turtle.setheading(180)
turtle.forward(lineWidth)
turtle.end_fill()

turtle.penup()
turtle.forward(lineWidth * 1.5)
turtle.pendown()
turtle.begin_fill()
turtle.forward(lineWidth)
turtle.setheading(120)
turtle.forward(lineWidth * 2.5)
turtle.setheading(60)
turtle.forward(lineWidth)
turtle.setheading(300)
turtle.forward(lineWidth * 3.5)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint)
turtle.setheading(90)
turtle.forward(lineWidth / 2)
turtle.setheading(180)
turtle.forward(lineWidth / 2)
ReturnPoint = turtle.position()
turtle.pendown()
turtle.begin_fill()
turtle.setheading(120)
turtle.forward(lineWidth)
turtle.setheading(0)
turtle.forward(letterHeight * 3/4)
turtle.setheading(240)
turtle.forward(lineWidth)
turtle.setheading(180)
turtle.forward(turtle.distance(ReturnPoint) )
turtle.end_fill()

turtle.penup()
turtle.setheading(120)
turtle.forward(lineWidth * 1.5)
turtle.pendown()
turtle.begin_fill()
ReturnPoint = turtle.position()
turtle.forward(lineWidth)
turtle.setheading(60)
turtle.forward(lineWidth)
rightWall = turtle.xcor()
turtle.setheading(300)
turtle.forward(lineWidth)
turtle.setheading(0)
turtle.forward(lineWidth * 2)
turtle.setheading(300)
turtle.forward(lineWidth)
turtle.setheading(180)
turtle.forward(turtle.distance(ReturnPoint) )
turtle.end_fill()
#END

turtle.done()