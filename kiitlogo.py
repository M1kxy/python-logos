# importing turtle for graphics
import turtle

# Forming the window screen
tut = turtle.Screen()

# background color green
tut.bgcolor("Black")

# object
pen = turtle.Turtle()
pen2 = turtle.Turtle()
pen3 = turtle.Turtle()
#speed of pen
pen.speed(20)
pen2.speed(20)
pen3.speed(20)
# object color
pen.color("Green")
pen2.color("Green")
pen3.color("Green")
# object width
pen.width(3)
pen2.width(3)
pen3.width(8)
tut = turtle.Screen()
pen.hideturtle()
pen2.hideturtle()
pen3.hideturtle()
#adjustments 
pen.penup()
pen.backward(200)
pen.pendown()
# Code for symbol

# k
pen.forward(20)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(50)
pen.left(30)

pen.forward(60)
pen.left(60)
pen.forward(20)
pen.left(120)
pen.forward(58)

pen.penup()

pen.left(60)
pen.forward(22)
pen.right(120)

pen.pendown()

pen.forward(60)
pen.right(60)
pen.forward(20)
pen.right(120)
pen.forward(58)
pen.left(120)

#move from letter
pen.penup()
pen.forward(70)
pen.pendown()

# i
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(70)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(20)
pen.left(90)

#move from letter
pen.penup()
pen.forward(50)
pen.pendown()

# i
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(70)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(20)
pen.left(90)

#move from letter
pen.penup()
pen.forward(50)
pen.pendown()

#t
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(80)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(30)
pen.left(90)
pen.forward(80)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(50)

#move from dots
pen2.penup()
pen2.backward(110)
pen2.right(90)
pen2.forward(10)
pen2.pendown()

#i dots
pen2.width(1)
pen2.fillcolor("Green")
pen2.begin_fill() 
pen2.circle(10)
pen2.end_fill()

#move from dots
pen2.penup()
pen2.left(90)
pen2.forward(50)
pen2.right(90)
pen2.pendown()

#i dots
pen2.fillcolor("Green")
pen2.begin_fill() 
pen2.circle(10)
pen2.end_fill()


#move from dots

pen2.penup()
pen2.left(90)
pen2.forward(50)

#i dots


#move
pen3.penup()
pen3.backward(190)
pen3.right(90)
pen3.forward(103)
pen3.pendown()

#underlines semicircle

pen3.left(30)
pen3.circle(120,120)

#move 
pen3.penup()
pen3.right(60)
pen3.backward(230)
pen3.pendown()
#underlines semicircle

pen3.right(65)
pen3.circle(140,130)

#move from
pen3.penup()
pen3.right(60)
pen3.backward(276)
pen3.right(66)#change this
pen3.pendown()

#final semicircle

i = 1
for i in range (7):
    pen3.circle(360,5)

    pen3.fillcolor("Green")
    pen3.begin_fill() 

    pen3.right(79)#change this
    pen3.forward(40)
    pen3.left(85)
    pen3.forward(10)
    pen3.left(85)
    pen3.forward(40)
    pen3.right(79)#change this
    pen3.end_fill()
pen3.circle(280,7)
turtle.done()
