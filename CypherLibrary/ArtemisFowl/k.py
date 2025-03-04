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
turtle.setheading(180)
turtle.circle(letterHeight / 12, 180)
turtle.setheading(270)
turtle.forward(letterHeight / 6)
turtle.setheading(0)
turtle.forward(letterHeight / 6)
returnPoint = turtle.position()
turtle.circle(-letterHeight / 12, 90)
radialStartPoint = turtle.position()
turtle.circle(-letterHeight / 12, 90)
turtle.forward(letterHeight / 6)

turtle.penup()
turtle.goto(returnPoint)
turtle.pendown()
turtle.setheading(270)
turtle.circle(-letterHeight / 6, 90)
returnPoint1 = turtle.position()
turtle.circle(-letterHeight / 4, 180)
turtle.circle(-letterHeight / 6, 90)

turtle.penup()
turtle.goto(returnPoint1)
turtle.pendown()
turtle.setheading(75)
turtle.circle(-letterHeight, 15)
radialEndPoint = turtle.position()
turtle.circle(-letterHeight, 14)
rightWall = turtle.xcor()

turtle.penup()
turtle.goto(returnPoint)
turtle.setheading(270)
turtle.circle(-letterHeight / 6, 47)
turtle.pendown()
turtle.setheading(75)
turtle.circle(-letterHeight * (5/6), 29)

turtle.penup()
turtle.goto(radialStartPoint)
turtle.pendown()
turtle.goto(radialEndPoint)

turtle.goto(radialStartPoint)
turtle.setheading(315)
turtle.circle(letterHeight / 3, 39)

turtle.penup()
turtle.goto(radialStartPoint)
turtle.pendown()
turtle.setheading(45)
turtle.circle(-letterHeight / 3, 39)
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()