# Charlette-Mhaye Derewecki
# 11/16/26
# P4LAB1
# Writing a turtle graphics program that draws a triangle and a square using loops

#Import the library
import turtle

#create the turtle window and drawing object
win = turtle.Screen ()
win.bgcolor("lightblue")
pen = turtle.Turtle()


#Set turtle options
pen.pensize(5)
pen.color("lightgreen")
pen.shape("turtle")

#Code to draw the shapes
for side in range (4) :
    pen.forward(200)
    pen.left(90)

#Move turtle to top-left corner of square
pen.left(90)
pen.forward(200)
pen.right(90)

#While loop that executes 3 times
pen.fillcolor("pink")
pen.begin_fill()
sides = 3

while sides > 0:
    pen.forward(200)
    pen.left(120)
    sides = sides - 1

pen.end_fill()
# wait for user to close window
win.mainloop()