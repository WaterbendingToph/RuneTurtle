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

turtle.goto(0, 0)
turtle.pendown()


#START
turtle.setheading(90)
turtle.begin_fill()
turtle.circle(letterHeight / 10)
turtle.end_fill()

turtle.setheading(180)
turtle.penup()
turtle.forward(letterHeight / 4 - letterHeight / 10)
turtle.pendown()
turtle.setheading(90)
turtle.circle(letterHeight / 4, 180)
returnPoint = turtle.position()
turtle.circle(letterHeight / 4, 180)

turtle.penup()
turtle.goto(returnPoint)
turtle.pendown()
turtle.setheading(270)
turtle.circle(letterHeight * (2/3) , 60)

turtle.penup()
turtle.goto(returnPoint)
turtle.setheading(90)
turtle.pendown()
turtle.circle(-letterHeight * (2/3) , 60)
rightWall = turtle.xcor()
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()