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
ReturnPoint = turtle.position()
turtle.setheading(120)
turtle.forward(lineWidth)
rightWall = turtle.xcor()
turtle.setheading(0)
turtle.forward(letterHeight * 3/4)
turtle.setheading(240)
turtle.forward(lineWidth)
ReturnPoint1 = turtle.position()
turtle.setheading(180)
turtle.forward(turtle.distance(ReturnPoint) ) 
turtle.end_fill()

turtle.penup()
turtle.backward(lineWidth) 
turtle.setheading(270)
turtle.forward(lineWidth / 2)
turtle.pendown()
turtle.begin_fill()
ReturnPoint = turtle.position()
endPointX = turtle.xcor()
turtle.setheading(240)
turtle.forward(lineWidth)
turtle.setheading(300)
turtle.forward(lineWidth)
turtle.setheading(60)
while turtle.xcor() < endPointX:
    turtle.forward(1)
turtle.setheading(180)
verticalOffset = turtle.distance(ReturnPoint)
turtle.forward(verticalOffset)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint1)
turtle.setheading(240)
turtle.forward(lineWidth * 1.5)
endPointY = turtle.ycor()
turtle.backward(lineWidth)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(180)
turtle.forward(turtle.distance(ReturnPoint) - verticalOffset - lineWidth /2)
turtle.setheading(240)
turtle.forward(lineWidth)
turtle.setheading(300)
turtle.forward(lineWidth)
turtle.setheading(60)
turtle.forward(lineWidth)
turtle.setheading(0)
turtle.forward(endPointY - turtle.ycor() )
turtle.setheading(60)
turtle.forward(lineWidth)
turtle.end_fill()
#END

turtle.done()