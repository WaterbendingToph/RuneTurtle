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
turtle.setheading(180)
turtle.forward(letterHeight / 6)
turtle.setheading(50)
turtle.circle(int(-letterHeight / 6), 215, int(letterHeight / 4) ) 
turtle.circle(int(letterHeight / 6), 250, int(letterHeight / 4) )
#END

turtle.done()