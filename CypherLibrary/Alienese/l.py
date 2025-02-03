import turtle
window = turtle.Screen()
window.setup(width = 600, height=600)

letterHeight = 500
dotWidth = letterHeight / 20
lowerLetterHeight = letterHeight * (2 / 3)

turtle.mode("logo")
turtle.penup()
turtle.pencolor("red")
turtle.goto(-300, -250)
turtle.pendown()
turtle.setheading(90)
turtle.forward(600)
turtle.penup()
turtle.goto(166, -300)
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.penup()
turtle.goto(300, 83)
turtle.pendown()
turtle.setheading(270)
turtle.forward(600)
turtle.penup()
turtle.goto(-166, 300)
turtle.pendown()
turtle.setheading(180)
turtle.forward(600)
turtle.penup()
turtle.pencolor("blacK")

turtle.goto(0, -letterHeight / 2)
turtle.pendown()


#START
turtle.penup()
turtle.goto(turtle.position()[0] - lowerLetterHeight / 2 + lowerLetterHeight / 10, turtle.position()[1] + lowerLetterHeight / 10)
turtle.pendown()
turtle.setheading(60)
turtle.circle(lowerLetterHeight * (3 / 5), 75)
turtle.circle(lowerLetterHeight / 6, 150)
turtle.circle(lowerLetterHeight / 3, 60)
turtle.circle(lowerLetterHeight * (1 / 2), 90)
turtle.circle(lowerLetterHeight / 3, 60)
turtle.circle(lowerLetterHeight / 6, 150)
turtle.circle(lowerLetterHeight * (3 / 5), 75)
#END

turtle.done()