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

turtle.goto(0, -125)
turtle.pendown()

#START
verticalInnerLength = letterHeight / 2 - 2 * lineWidth
outerLength = ( (letterHeight / 4) ** 2 + (verticalInnerLength / 2 + lineWidth) ** 2) ** (0.5)
innerLegnth = ( ( (verticalInnerLength / 2) ** 2) + ( (verticalInnerLength / 2) ) ** 2) ** (0.5)

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
turtle.pendown()
turtle.begin_fill()
turtle.setheading(135)
turtle.forward(outerLength)
turtle.setheading(225)
turtle.forward(outerLength)
turtle.setheading(135)
turtle.forward(outerLength)
turtle.setheading(225)
turtle.forward(outerLength)
turtle.setheading(0)
turtle.forward(lineWidth)
turtle.setheading(45)
turtle.forward(innerLegnth)
turtle.setheading(315)
turtle.forward(innerLegnth)
turtle.setheading(0)
turtle.forward(lineWidth * 2)
turtle.setheading(45)
turtle.forward(innerLegnth)
turtle.setheading(315)
turtle.forward(innerLegnth)
turtle.end_fill()
#END

turtle.done()