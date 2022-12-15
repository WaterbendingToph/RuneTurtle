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

turtle.goto(-125, -120)
turtle.pendown()

#START
turtle.setheading(107)
turtle.circle(int (letterHeight * (3/8) ), int(360 * (3/5) ), int(letterHeight / 2) )
turtle.setheading(0)
turtle.forward(letterHeight / 4)
#END

turtle.done()