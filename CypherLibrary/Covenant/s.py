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
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(largeSide)
turtle.setheading(330)
turtle.forward(largeSide)
turtle.setheading(210)
turtle.forward(largeSide / 4)
turtle.setheading(120)
turtle.circle(-largeSide / 4, 180, int(largeSide / 4) )
turtle.setheading(210)
turtle.forward(largeSide / 4)
turtle.end_fill()
#END

turtle.done()