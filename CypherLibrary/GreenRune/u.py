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

turtle.goto(-125, 75)
turtle.pendown()

#START
startingPoint = turtle.position()
turtle.setheading(45)
turtle.circle(int(-letterHeight * (2 / 5) ), 285, int(letterHeight / 4) )
turtle.penup()
turtle.goto(startingPoint)
turtle.pendown()
turtle.setheading(37)
turtle.circle(int(-letterHeight * (1 / 2) ), 302, int(letterHeight / 4) )
turtle.penup()
turtle.goto(0, 0)
#END

turtle.done()