import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterWidth = 250
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
turtle.goto(-125, -250)
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

turtle.goto(0, -125)
turtle.pendown()

#START
outerLine = (2 * (letterHeight ** 2) ) ** (0.5)
innerLine = (2 * ( (letterHeight - lineWidth - (lineWidth * 1.5) ) ** (2) ) ) ** (0.5)

turtle.penup()
turtle.setheading(270)
turtle.forward(letterHeight / 2)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(letterHeight)
turtle.setheading(135)
turtle.forward(outerLine)
turtle.setheading(270)
turtle.forward(lineWidth * 1.5)
turtle.setheading(315)
turtle.forward(innerLine)
turtle.setheading(180)
turtle.forward(letterHeight - lineWidth - (lineWidth * 1.5) )
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.end_fill()
#END

turtle.done()