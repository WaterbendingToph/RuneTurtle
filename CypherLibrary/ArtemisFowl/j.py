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

turtle.goto(0, -250)
turtle.pendown()


#START
turtle.setheading(90)
turtle.circle(letterHeight / 4, 90)
rightWall = turtle.xcor()
turtle.circle(letterHeight / 4, 50)
returnPoint1Right = turtle.position()
returnPoint1RightDirection = turtle.heading()
turtle.penup()
turtle.circle(letterHeight / 4, 80)
turtle.pendown()
turtle.circle(letterHeight / 4, 140)

turtle.penup()
turtle.setheading(0)
turtle.forward(letterHeight / 4  - letterHeight / 6)
turtle.pendown()
turtle.setheading(90)
turtle.circle(letterHeight / 6, 152)
turtle.penup()
turtle.circle(letterHeight / 6, 58)
turtle.pendown()
turtle.circle(letterHeight / 6, 150)


turtle.penup()
turtle.goto(returnPoint1Right)
turtle.pendown()
turtle.setheading(returnPoint1RightDirection + 100)             #  270 - (returnPoint1RightDirection - 270) 
turtle.circle(letterHeight / 4, 100)
turtle.penup()
returnPoint2Right = turtle.position()
returnPoint2RightDirection = turtle.heading()
turtle.circle(letterHeight / 4, 80)
turtle.pendown()
turtle.circle(letterHeight / 4, 140)
returnPoint = turtle.position()
turtle.circle(letterHeight / 4, 40)

turtle.penup()
turtle.goto(returnPoint)
turtle.setheading(0)
turtle.forward(letterHeight / 4 - letterHeight / 6)
turtle.pendown()
turtle.setheading(90)
turtle.circle(letterHeight / 6, 152)
turtle.penup()
turtle.circle(letterHeight / 6, 58)
turtle.pendown()
turtle.circle(letterHeight / 6, 150)

turtle.penup()
turtle.goto(returnPoint2Right)
turtle.setheading(returnPoint2RightDirection + 100)
turtle.pendown()
turtle.circle(letterHeight / 4, 320)
returnPoint = turtle.position()
turtle.circle(letterHeight / 4, 40)

turtle.penup()
turtle.goto(returnPoint)
turtle.setheading(0)
turtle.forward(letterHeight / 4 - letterHeight / 6)
turtle.pendown()
turtle.setheading(90)
turtle.circle(letterHeight / 6)

#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()