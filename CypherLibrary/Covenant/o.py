import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250
largeSide = int(letterHeight / 2)
smallerSide = int(letterHeight / 5)
ReturnPoint = 0,0

turtle.mode("logo")
turtle.penup()
turtle.pencolor("red")
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
turtle.goto(250, -125)
turtle.pendown()
turtle.setheading(270)
turtle.forward(500)

turtle.penup()
turtle.goto(-125, -250)
turtle.pendown()
turtle.setheading(0)
turtle.forward(500)

turtle.pencolor("black")
turtle.penup()

turtle.goto(-125, -125)
turtle.setheading(45)
turtle.forward( ( ( (2 * (letterHeight ** 2) ) ** (0.5) ) / 2) - ( (2 * ( (letterHeight / 4) ** 2) ) ** (0.5) ) )
turtle.pendown()

#START
turtle.penup()
turtle.setheading(90)
turtle.forward(smallerSide)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(largeSide / 2)
ReturnPoint = turtle.position()
turtle.forward(largeSide / 2)
turtle.setheading(120)
turtle.forward(largeSide)
turtle.setheading(240)
turtle.forward(largeSide / 4)
turtle.setheading(330)
turtle.circle(largeSide / 4, 180, int(largeSide / 4) )
turtle.setheading(240)
turtle.forward(largeSide / 4)
turtle.end_fill()

turtle.penup()
turtle.goto(ReturnPoint)
turtle.setheading(270)
turtle.forward(smallerSide / 2)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(smallerSide)
turtle.setheading(240)
turtle.forward(smallerSide)
turtle.setheading(120)
turtle.forward(smallerSide)
turtle.end_fill()
#END

turtle.done()