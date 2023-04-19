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
yValue = turtle.ycor()
turtle.setheading(30)
endValue = turtle.xcor() + lineWidth
while turtle.xcor() < endValue:
    turtle.forward(1)
rightWall = turtle.xcor()
turtle.setheading(0)
turtle.forward( (letterHeight * 0.6) - (turtle.ycor() - yValue) ) 
turtle.begin_fill()
turtle.forward(lineWidth)
turtle.setheading(210)
endValue = turtle.xcor() - lineWidth
while turtle.xcor() > endValue:
    turtle.forward(1)
turtle.setheading(180)
turtle.forward(lineWidth)
turtle.setheading(30)
endValue = turtle.xcor() + lineWidth
while turtle.xcor() < endValue:
    turtle.forward(1)
turtle.end_fill()
turtle.setheading(0)
turtle.forward(letterHeight * 0.4)
turtle.setheading(270)
turtle.forward(lineWidth)
turtle.setheading(180)
turtle.forward(letterHeight)
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()