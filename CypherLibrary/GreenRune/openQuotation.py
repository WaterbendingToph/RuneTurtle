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

turtle.goto(-125, -125)
turtle.pendown()

#START
turtle.penup()
turtle.setheading(90)
turtle.forward(letterHeight / 2)
turtle.pendown()
turtle.setheading(270)
turtle.circle(-letterHeight / 2, 180, 2)
#END

turtle.done()