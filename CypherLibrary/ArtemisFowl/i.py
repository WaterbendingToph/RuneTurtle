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
turtle.setheading(270)
turtle.circle(-letterHeight / 4, 30)
turtle.circle(-letterHeight / 3, 30)
turtle.circle(-letterHeight / 2, 30)
returnPoint = turtle.position()
turtle.circle(-letterHeight / 2, 30)
turtle.circle(-letterHeight / 3, 30)
turtle.circle(-letterHeight / 4, 30)
returnPoint1 = turtle.position()
turtle.circle(-letterHeight / 4, 30)
turtle.circle(-letterHeight / 3, 30)
turtle.circle(-letterHeight / 2, 30)
returnPoint2 = turtle.position()
rightWall = turtle.xcor()
turtle.circle(-letterHeight / 2, 30)
turtle.circle(-letterHeight / 3, 30)
turtle.circle(-letterHeight / 4, 30)

turtle.penup()
turtle.goto(returnPoint1)
turtle.setheading(270)
startingXCor = turtle.xcor()
turtle.circle(letterHeight / 4, 10)
turtle.pendown()
turtle.setheading(15)
count = 0
while turtle.xcor() < startingXCor:
    turtle.forward(1)
    count += 1
turtle.setheading(165)
turtle.forward(count)

turtle.penup()
turtle.goto(returnPoint)
turtle.pendown()
turtle.setheading(90)
turtle.forward(returnPoint2[0] - returnPoint[0] )
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()