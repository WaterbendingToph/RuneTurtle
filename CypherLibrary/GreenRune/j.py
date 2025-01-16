import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

turtle.mode("logo")
turtle.penup()
turtle.pencolor("red")
turtle.goto(-250, 125)
turtle.pendown()
turtle.setheading(90)
turtle.forward(500)
turtle.penup()
turtle.goto(-250, -125)
turtle.pendown()
turtle.setheading(90)
turtle.forward(500)
turtle.pencolor("black")
turtle.penup()

turtle.goto(125, 125)
turtle.pendown()

#START
turtle.setheading(90)
turtle.penup()
turtle.backward(letterHeight / 4)
turtle.pendown()
turtle.forward(letterHeight / 4)
turtle.setheading(270)
turtle.forward(letterHeight / 8)
turtle.setheading(180)
turtle.forward(letterHeight * (2 / 3) )
turtle.circle(int(-letterHeight / 3), 135, int(letterHeight / 3) )
turtle.setheading(45)
turtle.forward(letterHeight / 8)
turtle.setheading(225)
turtle.forward(letterHeight / 4)
#END

turtle.done()