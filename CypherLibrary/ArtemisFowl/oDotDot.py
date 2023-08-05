import turtle
window = turtle.Screen()
window.setup(width = 600, height=600)

letterHeight = 400
lineWidth = 20
rightWall = 0
returnPoint = 0,0

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
startingYCor = turtle.ycor()
startingXCor = turtle.xcor()
turtle.setheading(90)
turtle.circle(lineWidth * 3, 90)
rightWall = turtle.xcor()
turtle.setheading(0)
turtle.circle(lineWidth, 90)
turtle.circle(-lineWidth, 90)
turtle.setheading(0)
turtle.forward(letterHeight / 2)
yCorReturnPoint = turtle.ycor()
returnPoint = turtle.position()
turtle.setheading(45)
turtle.circle(lineWidth, 270)
turtle.setheading(180)
turtle.forward(turtle.ycor() - startingYCor)
turtle.setheading(90)
turtle.forward(startingXCor - turtle.xcor() )

turtle.penup()
turtle.goto(returnPoint)
turtle.setheading(315)
turtle.forward(lineWidth / 2)
turtle.pendown()
turtle.setheading(30)
turtle.circle(lineWidth / 2, 360, 3)
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()