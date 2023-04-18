import turtle
window = turtle.Screen()
window.setup(width = 600, height=600)

letterHeight = 400
lineWidth = 20
rightWall = 0
returnPoint = 0,0

turtle.mode("logo")
turtle.penup()
turtle.pencolor("red")
turtle.goto(-300, -250)
turtle.pendown()
turtle.setheading(90)
turtle.forward(600)
turtle.penup()
turtle.goto(250, -300)
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.penup()
turtle.goto(300, 250)
turtle.pendown()
turtle.setheading(270)
turtle.forward(600)
turtle.penup()
turtle.goto(-250, 300)
turtle.pendown()
turtle.setheading(180)
turtle.forward(600)
turtle.penup()
turtle.pencolor("blacK")

turtle.goto(0, -letterHeight / 2)
turtle.pendown()


#START
turtle.setheading(300)
turtle.forward(letterHeight / 2)
turtle.setheading(60)
turtle.forward(letterHeight / 2)
turtle.setheading(180)
turtle.forward(letterHeight / 2)
turtle.setheading(60)
turtle.forward(letterHeight / 2)
turtle.setheading(300)
turtle.forward(letterHeight)
turtle.setheading(180)
turtle.forward(letterHeight / 2)
turtle.setheading(60)
turtle.forward(letterHeight)
turtle.setheading(180)
turtle.forward(letterHeight / 2)
turtle.setheading(300)
turtle.forward(letterHeight)
turtle.setheading(60)
turtle.forward(letterHeight / 2)
turtle.setheading(180)
turtle.forward(letterHeight / 2)
turtle.setheading(60)
turtle.forward(letterHeight / 2)
turtle.setheading(300)
turtle.forward(letterHeight / 2)
#END

turtle.done()