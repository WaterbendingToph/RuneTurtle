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
turtle.setheading(0)
turtle.forward(letterHeight * 2/3)
turtle.setheading(60)
initialY = turtle.ycor()
endPointX = turtle.xcor() + lineWidth
while turtle.xcor() < endPointX:
    turtle.forward(1)
verticalOffset = turtle.ycor() - initialY
turtle.setheading(180)
turtle.forward(letterHeight * 2/3 + verticalOffset)
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.end_fill()

turtle.penup()
turtle.setheading(90)
turtle.forward(lineWidth * 1.5)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(letterHeight / 3)
initialY = turtle.ycor()
turtle.setheading(60)
endPointX = turtle.xcor() + lineWidth
while turtle.xcor() < endPointX:
    turtle.forward(1)
verticalOffset = turtle.ycor() - initialY
turtle.setheading(180)
turtle.forward(letterHeight / 3 + verticalOffset - lineWidth)
turtle.setheading(90)
turtle.forward(lineWidth)
turtle.setheading(150)
initialX = turtle.xcor()
endPointY = turtle.ycor() - lineWidth
while turtle.ycor() > endPointY:
    turtle.forward(1)
horizontalOffset = turtle.xcor() - initialX
rightWall = turtle.xcor()
turtle.setheading(270)
turtle.forward(horizontalOffset + lineWidth + lineWidth)
turtle.end_fill()
#END

turtle.done()