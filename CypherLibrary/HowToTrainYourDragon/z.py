import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterWidth = 200
lineWidth = 20
letterHeight = 250
diagonal = 60

halfVertical = 0.7 * letterHeight
diagonalLineWidth = lineWidth * 1.5
verticalStarter = letterHeight / 4
obnoxiousLineSegment = halfVertical - lineWidth - diagonalLineWidth - verticalStarter
secondObnoxiousLineSegment = verticalStarter + lineWidth

turtle.mode("logo")
turtle.penup()
turtle.goto(-10, -125)
turtle.pendown()

turtle.begin_fill()
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.setheading(0)
turtle.forward(verticalStarter)
turtle.setheading(225)
turtle.forward(diagonal)
turtle.setheading(0)
turtle.forward(diagonalLineWidth)
turtle.setheading(45)
turtle.forward(diagonal)
turtle.setheading(0)
turtle.forward(obnoxiousLineSegment)
turtle.setheading(225)
turtle.forward(diagonal * 2)
turtle.setheading(0)
turtle.forward(obnoxiousLineSegment + lineWidth)
turtle.setheading(225)
turtle.forward(diagonal)
turtle.setheading(0)
turtle.forward(diagonalLineWidth)
turtle.setheading(45)
turtle.forward(diagonal)
turtle.setheading(0)
turtle.forward(secondObnoxiousLineSegment)
turtle.setheading(90)
turtle.forward(lineWidth)
turtle.setheading(180)
turtle.forward(verticalStarter)
turtle.setheading(45)
turtle.forward(diagonal)
turtle.setheading(180)
turtle.forward(diagonalLineWidth)
turtle.setheading(225)
turtle.forward(diagonal)
turtle.setheading(180)
turtle.forward(obnoxiousLineSegment)
turtle.setheading(45)
turtle.forward(diagonal * 2)
turtle.setheading(180)
turtle.forward(lineWidth + obnoxiousLineSegment)
turtle.setheading(45)
turtle.forward(diagonal)
turtle.setheading(180)
turtle.forward(diagonalLineWidth)
turtle.setheading(225)
turtle.forward(diagonal)
turtle.setheading(180)
turtle.forward(secondObnoxiousLineSegment)
turtle.end_fill()

turtle.done()