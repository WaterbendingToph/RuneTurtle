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
turtle.goto(turtle.position()[0] + dotWidth, turtle.position()[1] + dotWidth)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.circle(-dotWidth)
turtle.end_fill()

turtle.penup()
turtle.goto(turtle.position()[0] - dotWidth, turtle.position()[1] - dotWidth)
turtle.pendown()
turtle.goto(turtle.position()[0] - lowerLetterHeight / 2, turtle.position()[1] + lowerLetterHeight / 4)
turtle.goto(turtle.position()[0] + lowerLetterHeight * (2 / 3), turtle.position()[1] - (lowerLetterHeight / 4 - lowerLetterHeight / 6) )
turtle.setheading(270 + 23)
turtle.forward(lowerLetterHeight / 3)
turtle.circle(-lowerLetterHeight / 3, 240)
turtle.circle(-lowerLetterHeight * (3 / 12), 90)
turtle.circle(-lowerLetterHeight * (3 / 24), 90)
turtle.circle(-lowerLetterHeight * (3 / 24), 90)
#END

turtle.done()