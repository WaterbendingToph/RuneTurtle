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
turtle.goto(turtle.position()[0], turtle.position()[1] + lowerLetterHeight)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(270)
turtle.circle(dotWidth)
turtle.end_fill()
turtle.goto(turtle.position()[0], turtle.position()[1] - lowerLetterHeight / 3 + dotWidth)
turtle.setheading(180)
turtle.circle(-dotWidth, 90)
turtle.forward(lowerLetterHeight / 2 - dotWidth * 2)
turtle.circle(dotWidth, 90)
turtle.forward(lowerLetterHeight / 12)
turtle.circle(lowerLetterHeight / 2, 180)
turtle.forward(lowerLetterHeight / 12)
turtle.circle(dotWidth, 90)
turtle.forward(lowerLetterHeight / 2 - dotWidth * 2)
turtle.circle(-dotWidth, 90)

turtle.penup()
turtle.goto(turtle.position()[0] - lowerLetterHeight / 4 + dotWidth * 2, turtle.position()[1] - dotWidth * 4)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(315)
for x in range(2):
    turtle.circle(dotWidth * 2, 90)
    turtle.circle(dotWidth, 90)
turtle.end_fill()

turtle.penup()
turtle.goto(turtle.position()[0] + lowerLetterHeight / 2 - dotWidth * 4, turtle.position()[1] )
turtle.pendown()
turtle.begin_fill()
turtle.setheading(45)
for x in range(2):
    turtle.circle(-dotWidth * 2, 90)
    turtle.circle(-dotWidth, 90)
turtle.end_fill()
#END

turtle.done()