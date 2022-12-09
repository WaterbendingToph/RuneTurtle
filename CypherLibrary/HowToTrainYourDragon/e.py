import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterWidth = 200
lineWidth = 20
letterHeight = 250
diagonal = 60

turtle.mode("logo")
turtle.penup()
turtle.goto(-10, -125)
turtle.pendown()

turtle.begin_fill()
turtle.setheading(90)
turtle.forward(lineWidth)
turtle.setheading(0)
turtle.forward(letterHeight)
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.setheading(180)
turtle.forward(letterHeight)
turtle.end_fill()

turtle.penup()
turtle.setheading(0)
turtle.forward(letterHeight / 2)
turtle.setheading(90)
turtle.forward(lineWidth * 2)
turtle.setheading(0)
turtle.begin_fill()
turtle.circle(lineWidth * 1.5, steps=lineWidth * 2)
turtle.end_fill()

turtle.done()