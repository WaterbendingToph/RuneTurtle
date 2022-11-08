# note to self: the commented out lines were the originals, I rewrote it to run all at the same speed as an academic exercise 

import turtle
wn = turtle.Screen()
wn.setup(width=400, height=400)
red = turtle.Turtle()

def curve():
    # for i in range(200):
    #     red.right(1)
    #     red.forward(1)
    red.circle(-50, 200)

def heart():
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    # red.forward(113)
    red.forward(98)
    curve()
    red.left(120)
    curve()
    # red.forward(112)
    red.forward(100)
    red.end_fill()

heart()
red.ht()
turtle.done()