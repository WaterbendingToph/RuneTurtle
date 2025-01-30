import turtle
window = turtle.Screen()
window.setup(width = 600, height=600)

letterHeight = 500
dotWidth = letterHeight / 20

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
letterEndPoint = (turtle.position()[0] + letterHeight / 2, turtle.position()[1] )
turtle.penup()
turtle.goto(turtle.position()[0], turtle.position()[1] + letterHeight / 2)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(270)
turtle.circle(dotWidth)
turtle.end_fill()
turtle.goto(turtle.position()[0], turtle.position()[1] - dotWidth)
turtle.circle(letterHeight / 2 - dotWidth, 270)
turtle.circle(letterHeight * (3 / 8) - dotWidth, 180)
turtle.goto(letterEndPoint)
#END

turtle.done()