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

turtle.goto(-125, 125)
turtle.pendown()

#START
turtle.penup()
turtle.setheading(180)
turtle.forward(3 * letterHeight / 5)
turtle.pendown()
turtle.setheading(90)
turtle.forward(letterHeight / 3)
turtle.setheading(0)
turtle.circle(int(-letterHeight / 6), 180, int(letterHeight / 6) )
turtle.setheading(90)
turtle.forward(letterHeight / 3)
turtle.penup()
turtle.setheading(180)
turtle.forward(letterHeight / 4)
turtle.setheading(270)
turtle.pendown()
turtle.forward(letterHeight)
#END

turtle.done()