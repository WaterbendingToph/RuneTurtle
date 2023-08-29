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

turtle.goto(letterHeight / 4, -letterHeight / 4)
turtle.pendown()


#START
turtle.begin_fill()
turtle.setheading(270)
turtle.circle(-letterHeight / 4, 90)
turtle.circle(-letterHeight / 6, 60)
turtle.circle(letterHeight / 6, 150)
topPoint = turtle.position()

turtle.setheading(90)
turtle.circle(-letterHeight / 4, 90)
turtle.circle(-letterHeight / 6, 60)
turtle.circle(letterHeight / 6, 150)
turtle.end_fill()

offsetY = (topPoint[1] - turtle.ycor() ) / 2
offsetX = (turtle.xcor() - topPoint[0] ) / 2
newY = offsetX + offsetY + turtle.ycor()
newX = turtle.xcor() - offsetX + offsetY

turtle.penup()
turtle.goto(newX, newY)
rightWall = turtle.xcor()
turtle.pendown()
turtle.begin_fill()
turtle.setheading(180)
turtle.circle(-letterHeight / 4, 90)
turtle.circle(-letterHeight / 6, 60)
turtle.circle(letterHeight / 6, 150)

turtle.setheading(0)
turtle.circle(-letterHeight / 4, 90)
turtle.circle(-letterHeight / 6, 60)
turtle.circle(letterHeight / 6, 150)
turtle.end_fill()
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()