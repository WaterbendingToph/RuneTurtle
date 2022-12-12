import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterWidth = 200
lineWidth = 20
letterHeight = 250
diagonal = 60

outerLine = (2 * (letterHeight ** 2) ) ** (0.5)
innerLine = (2 * ( (letterHeight - lineWidth - (lineWidth * 1.5) ) ** (2) ) ) ** (0.5)

turtle.mode("logo")
turtle.penup()
turtle.goto(-10, -125)
turtle.pendown()

#START
turtle.begin_fill()
turtle.setheading(270)
turtle.forward(lineWidth)
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
turtle.end_fill()
#END

turtle.done()