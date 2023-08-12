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
middleXValue = turtle.xcor()
turtle.setheading(90)
turtle.forward(letterHeight / 8)
turtle.setheading(0)
turtle.forward(letterHeight)
turtle.setheading(270)
turtle.forward(letterHeight / 4)
turtle.setheading(180)
turtle.forward(letterHeight)
turtle.setheading(90)
turtle.forward(letterHeight / 4)

turtle.setheading(0)
turtle.forward(letterHeight / 12)
turtle.setheading(90)
returnPoint = turtle.position()
turtle.circle(letterHeight / 6, 90)
rightWall = turtle.xcor()
turtle.circle(letterHeight / 6, 60)
straightMoveLength = 0
while turtle.xcor() > middleXValue:
    turtle.forward(1)
    straightMoveLength += 1
turtle.forward(straightMoveLength)
turtle.circle(-letterHeight / 6, 60)
turtle.circle(-letterHeight / 6, 90)

turtle.forward(middleXValue - turtle.xcor() + letterHeight / 8)
turtle.circle(-letterHeight / 6, 90)
turtle.circle(-letterHeight / 6, 60)
turtle.forward(straightMoveLength)
turtle.forward(straightMoveLength)
turtle.circle(letterHeight / 6, 60)
turtle.circle(letterHeight / 6, 90)
turtle.goto(returnPoint)
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()