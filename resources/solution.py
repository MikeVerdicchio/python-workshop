import turtle
PROGNAME = 'Sierpinski Carpet'

myPen = turtle.Turtle()
myPen.speed(30)
myPen.color("#000000")

# This function draws a box by drawing each side of the square and using the fill function
def box(boxSize, depth, start):
    #Position myPen in center of the screen
    myPen.penup()
    myPen.goto(start[0], start[1])
    myPen.pendown()

    myPen.begin_fill()
    # 0 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 90 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 180 deg.
    myPen.forward(boxSize)
    myPen.left(90)
    # 270 deg.
    myPen.forward(boxSize)
    myPen.end_fill()
    myPen.setheading(0)

    if depth > 0:
        #top left
        box(boxSize / 3, depth - 1, [start[0] - 0.66*boxSize, start[1] + 1.33*boxSize])

        #top mid
        box(boxSize / 3, depth - 1, [start[0] + 0.33*boxSize, start[1] + 1.33*boxSize])

        #top right
        box(boxSize / 3, depth - 1, [start[0] + 1.33*boxSize, start[1] + 1.33*boxSize])

        #right
        box(boxSize / 3, depth - 1, [start[0] + 1.33*boxSize, start[1] + 0.33*boxSize])

        #bottom right
        box(boxSize / 3, depth - 1, [start[0] + 1.33*boxSize, start[1] - 0.66*boxSize])

        #bottom mid
        box(boxSize / 3, depth - 1, [start[0] + 0.33*boxSize, start[1] - 0.66*boxSize])

        #bottom left
        box(boxSize / 3, depth - 1, [start[0] - 0.66*boxSize, start[1] - 0.66*boxSize])

        #left
        box(boxSize / 3, depth - 1, [start[0] - 0.66*boxSize, start[1] + 0.33*boxSize])
	

#draw the first box
box(100, 3, [-50, -50])
turtle.mainloop()
