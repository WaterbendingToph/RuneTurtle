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

turtle.goto(-letterHeight * (1/3), -letterHeight * (1/3) )
turtle.pendown()


#START
turtle.setheading(90)
turtle.begin_fill()
turtle.forward(letterHeight * (2/3) )
for x in range(8):
    turtle.setheading(180)
    turtle.circle(-letterHeight * (2/3) / 16, 180, 2)
turtle.end_fill()

turtle.begin_fill()
turtle.setheading(0)
turtle.forward(letterHeight * (2/3) )
for x in range(8):
    turtle.setheading(270)
    turtle.circle(letterHeight * (2/3) / 16, 180, 2)
turtle.end_fill()

turtle.penup()
turtle.goto(turtle.xcor() + letterHeight * (2/3), turtle.ycor() + letterHeight * (2/3) )
turtle.pendown()

turtle.begin_fill()
turtle.setheading(270)
turtle.forward(letterHeight * (2/3) )
for x in range(8):
    turtle.setheading(0)
    turtle.circle(-letterHeight * (2/3) / 16, 180, 2)
turtle.end_fill()

turtle.begin_fill()
turtle.setheading(180)
turtle.forward(letterHeight * (2/3) )
for x in range(7):
    turtle.setheading(90)
    turtle.circle(letterHeight * (2/3) / 16, 180, 2)
turtle.setheading(90)
turtle.circle(letterHeight * (2/3) / 16, 90, 1)
rightWall = turtle.xcor()
turtle.circle(letterHeight * (2/3) / 16, 90, 1)
turtle.end_fill()
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()