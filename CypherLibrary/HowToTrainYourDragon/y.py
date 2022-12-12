import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterWidth = 200
lineWidth = 20
letterHeight = 250
diagonal = 60
innerFlushDiagonal =  (2 * ( (letterHeight / 4) ** 2) ) ** (0.5)
outerFlushDiagonal = innerFlushDiagonal + ( (2 * (lineWidth * 1.5) ** 2) ** (0.5) )

turtle.mode("logo")
turtle.penup()
turtle.goto(-10, -125)
turtle.pendown()

#START
turtle.begin_fill()
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.setheading(0)
turtle.forward(letterHeight / 4)
turtle.setheading(225)
turtle.forward(innerFlushDiagonal)
turtle.setheading(270)
turtle.forward(lineWidth * 1.5)
turtle.setheading(45)
turtle.forward(outerFlushDiagonal)
turtle.setheading(0)
turtle.forward(letterHeight - (letterHeight / 4) - (lineWidth * 1.5) )
turtle.setheading(90)
turtle.forward(lineWidth)
turtle.setheading(180)
turtle.forward(letterHeight - (letterHeight / 4) - (lineWidth * 1.5) )
turtle.setheading(135)
turtle.forward(outerFlushDiagonal)
turtle.setheading(270)
turtle.forward(lineWidth * 1.5)
turtle.setheading(315)
turtle.forward(innerFlushDiagonal)
turtle.setheading(180)
turtle.forward(letterHeight / 4)
turtle.end_fill()
#END

turtle.done()