import turtle
window = turtle.Screen()
window.setup(width = 600, height=600)

letterHeight = 500
dotWidth = letterHeight / 20
lowerLetterHeight = letterHeight * (3 / 4)

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
turtle.begin_fill()
turtle.setheading(90)
turtle.circle(dotWidth)
turtle.end_fill()
turtle.setheading(5)
turtle.circle(-lowerLetterHeight * (3 / 4), 38)
turtle.setheading(138)
turtle.circle(lowerLetterHeight * (3 / 4), -37)
turtle.begin_fill()
turtle.setheading(270)
turtle.circle(dotWidth)
turtle.end_fill()
turtle.setheading(185)
turtle.circle(-lowerLetterHeight * (3 / 4), 38)
turtle.setheading(313)
turtle.circle(lowerLetterHeight * (3 / 4), -37)
#END

turtle.done()