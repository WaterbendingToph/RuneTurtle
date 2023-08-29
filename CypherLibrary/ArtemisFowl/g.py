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

turtle.goto(0, -letterHeight / 2)
turtle.pendown()


#START
turtle.setheading(90)
turtle.circle(letterHeight / 4, 75)
returnPoint = turtle.position()
turtle.circle(letterHeight / 2, 30)
turtle.circle(-letterHeight / 6, 105)

rightWall = turtle.xcor()
turtle.setheading(270)
turtle.circle(letterHeight / 3, 100)
turtle.circle(-letterHeight / 6, 44)
returnPoint1 = turtle.position()
turtle.circle(letterHeight / 4, 34)

turtle.penup()
turtle.goto(returnPoint)
turtle.pendown()
turtle.setheading(30)
turtle.forward(letterHeight / 8)
turtle.setheading(300)
turtle.forward(letterHeight / 20)

turtle.penup()
turtle.goto(returnPoint1)
turtle.pendown()
turtle.setheading(330)
turtle.forward(letterHeight / 8)
turtle.setheading(60)
turtle.forward(letterHeight / 10)
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()