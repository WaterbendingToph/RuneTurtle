import turtle
window = turtle.Screen()
window.setup(width = 600, height=600)

letterHeight = 400
diagonalLength = 0
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
turtle.forward(letterHeight * 3/4)
ReturnPoint = turtle.position()
turtle.setheading(240)
initialY = turtle.ycor()
endPointX = turtle.xcor() - lineWidth
while turtle.xcor() > endPointX:
    turtle.forward(1)
diagonalLength = turtle.distance(ReturnPoint)
verticalOffset = initialY - turtle.ycor()
turtle.setheading(180)
turtle.forward(letterHeight * 3/4 - verticalOffset * 2)
turtle.setheading(120)
turtle.forward(diagonalLength)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint)
turtle.setheading(60)
turtle.forward(diagonalLength / 2)
turtle.pendown()
turtle.begin_fill()
turtle.forward(diagonalLength)
rightWall = turtle.xcor()
turtle.setheading(180)
turtle.forward(letterHeight * 1/2 + verticalOffset * 2)
turtle.setheading(300)
turtle.forward(diagonalLength)
turtle.setheading(0)
turtle.forward(letterHeight * 1/2)
turtle.end_fill()
#END

turtle.done()