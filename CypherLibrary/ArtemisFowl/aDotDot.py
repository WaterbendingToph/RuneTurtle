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
initialXCor = turtle.xcor()
initialYCor = turtle.ycor()
endYCor = initialYCor + letterHeight / 3
arcLength = 0
while turtle.ycor() < endYCor:
    turtle.circle(letterHeight / 2, 1)
    arcLength += 1
rightWall = turtle.xcor()

turtle.penup()
turtle.goto(initialXCor, initialYCor)
turtle.pendown()
turtle.setheading(270)
turtle.circle(-letterHeight / 2, arcLength)

turtle.penup()
turtle.goto(initialXCor, initialYCor + 2 * letterHeight / 3)
returnPoint = turtle.position()
turtle.pendown()
turtle.setheading(90)
turtle.circle(-letterHeight / 2, arcLength)

turtle.penup()
turtle.goto(returnPoint)
turtle.pendown()
turtle.setheading(270)
turtle.circle(letterHeight / 2, arcLength)

turtle.penup()
turtle.goto(returnPoint)
turtle.pendown()
turtle.setheading(225)
turtle.begin_fill()
arcLength = 0 
endYCor = (turtle.ycor() - initialYCor) / 2 + initialYCor
while turtle.ycor() >= endYCor:
    turtle.circle(letterHeight / 2, 1)
    arcLength += 1
turtle.setheading(180)
turtle.circle(letterHeight / 2, arcLength)
turtle.setheading(45)
turtle.circle(letterHeight / 2, arcLength)
turtle.setheading(0)
turtle.circle(letterHeight / 2, arcLength)
turtle.end_fill()
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()