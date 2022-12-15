import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterWidth = 200
lineWidth = 20
letterHeight = 250
diagonal = 60

turtle.mode("logo")
turtle.penup()
turtle.pencolor("red")
turtle.goto(-250, -125)
turtle.pendown()
turtle.setheading(90)
turtle.forward(500)
turtle.penup()
turtle.goto(-100, -250)
turtle.pendown()
turtle.setheading(0)
turtle.forward(500)
turtle.penup()
turtle.goto(-250, 125)
turtle.pendown()
turtle.setheading(90)
turtle.forward(500)
turtle.penup()
turtle.goto(125, 250)
turtle.pendown()
turtle.setheading(180)
turtle.forward(500)
turtle.penup()
turtle.pencolor("blacK")

turtle.goto(-10, -125)
turtle.pendown()

#START
turtle.begin_fill()
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.setheading(0)
turtle.forward(letterHeight - (lineWidth * 1.5) )
turtle.setheading(225)
turtle.forward(diagonal)

circleStartingPoint = turtle.position()

turtle.setheading(0)
turtle.forward(lineWidth * 1.5)
turtle.setheading(45)
turtle.forward(diagonal)
turtle.setheading(90)
turtle.forward(lineWidth)
turtle.setheading(180)
turtle.forward(letterHeight)
turtle.end_fill()

turtle.penup()
turtle.goto(circleStartingPoint)
turtle.setheading(45)
turtle.forward(diagonal / 2)
turtle.setheading(180)
turtle.forward(lineWidth)
turtle.begin_fill()
turtle.setheading(270)
turtle.circle(lineWidth)
turtle.end_fill()
#END

turtle.done()