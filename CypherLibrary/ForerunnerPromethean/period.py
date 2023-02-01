import turtle
window = turtle.Screen()
window.setup(width = 600, height=600)

letterHeight = 400
lineWidth = 20
rightWall = 0
leftX = 0
leftY = 0
rightX = 0
rightY = 0
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
rightY = turtle.ycor()
rightX = turtle.xcor()
leftX = turtle.xcor() - lineWidth

turtle.begin_fill()
turtle.setheading(300)
while turtle.xcor() > leftX:
    turtle.forward(1)
turtle.setheading(60)
while turtle.xcor() < rightX:
    turtle.forward(1)
turtle.setheading(180)
while turtle.ycor() > rightY:
    turtle.forward(1)
turtle.end_fill()

rightWall = turtle.xcor()
#END

turtle.done()