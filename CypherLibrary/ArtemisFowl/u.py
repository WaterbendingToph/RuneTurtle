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

turtle.goto(-letterHeight / 2, -letterHeight / 2)
turtle.pendown()


#START
turtle.begin_fill()
turtle.setheading(90)
turtle.circle(letterHeight /2, 180)
turtle.setheading(90)
turtle.forward(lineWidth)
turtle.circle(-letterHeight  /2, 180)
turtle.end_fill()

turtle.setheading(270)
turtle.forward(lineWidth)
turtle.setheading(90)
turtle.forward(lineWidth * 3)
turtle.circle(letterHeight / 2, 90)
rightWall = turtle.xcor()
turtle.circle(letterHeight / 2, 90)
turtle.setheading(270)
turtle.forward(lineWidth * 2)
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()