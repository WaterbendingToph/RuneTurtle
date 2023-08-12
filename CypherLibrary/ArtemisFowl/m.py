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
returnPoint = turtle.position()
turtle.setheading(90)
turtle.forward(lineWidth)
turtle.setheading(0)
turtle.forward(letterHeight / 2)
turtle.setheading(90)
turtle.circle(lineWidth * 2, 45)
turtle.circle(lineWidth * 4, 45)
turtle.forward(lineWidth * 2)
rightWall = turtle.xcor()
turtle.setheading(270)
turtle.circle(lineWidth * 2, 45)
turtle.circle(lineWidth * 4, 45)
returnPoint1 = turtle.position()

turtle.penup()
turtle.goto(returnPoint)
turtle.pendown()
turtle.setheading(0)
turtle.forward(letterHeight / 2)
turtle.setheading(270)
turtle.circle(-lineWidth * 2, 45)
turtle.circle(-lineWidth * 4, 45)
turtle.forward(lineWidth * 2)
turtle.setheading(90)
turtle.circle(-1 * (returnPoint1[0] - turtle.xcor() ), 90)
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()