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

turtle.goto(-(letterHeight / 2 + lineWidth * 2) / 2, -lineWidth * 2)
turtle.pendown()


#START
StartingYCor = turtle.ycor()
turtle.begin_fill()
turtle.setheading(75)
turtle.forward(letterHeight / 2)
rightWall = turtle.xcor()
turtle.setheading(285)
turtle.forward(letterHeight / 2)
turtle.setheading(180)
turtle.circle(-lineWidth * 2, 90)
turtle.setheading(180)
turtle.forward(turtle.ycor() - StartingYCor - lineWidth * 2)
turtle.setheading(90)
turtle.circle(-lineWidth * 2, 90)
turtle.end_fill()
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()





