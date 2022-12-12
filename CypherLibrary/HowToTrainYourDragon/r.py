import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterWidth = 200
lineWidth = 20
letterHeight = 250

obnoxiousVerticalLength = letterHeight / 2 - lineWidth
topOuterDiagonal = (2 * ( (letterHeight / 4) ** 2) ) ** (0.5)
topInnerDiagonal =  ( 2 * ( (letterHeight / 4 - lineWidth) ** 2) ) ** (0.5) 
bottomOuterDiagonal = (2 * ( (letterHeight / 2) ** 2) ) ** (0.5)
bottomInnerDiagonal = ( ( 2 * (obnoxiousVerticalLength ** 2) ) ** (0.5) )


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
turtle.setheading(90)
turtle.forward(lineWidth)
startingPoint1 = turtle.position()
turtle.setheading(180)
turtle.forward(letterHeight)
turtle.end_fill()

turtle.penup()
turtle.goto(startingPoint1)
turtle.begin_fill()
turtle.pendown()
turtle.setheading(135)
turtle.forward(topOuterDiagonal)
turtle.setheading(225)
turtle.forward(topOuterDiagonal)
startingPoint2 = turtle.position()
turtle.setheading(0)
turtle.forward(lineWidth)
turtle.setheading(45)
turtle.forward(topInnerDiagonal)
turtle.setheading(315)
turtle.forward(topInnerDiagonal)
turtle.end_fill()
turtle.penup()

turtle.goto(startingPoint2)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(135)
turtle.forward(bottomOuterDiagonal)
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.setheading(315)
turtle.forward(bottomInnerDiagonal)
turtle.setheading(0)
turtle.forward(lineWidth)
turtle.end_fill()
#END

turtle.done()