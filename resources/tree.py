import turtle
def tree(f_length, min_length=2):
    """
    Draws a tree with 2 branches using recursion
    """
    turtle.forward(f_length)
    if f_length > min_length:
        turtle.left(45)
        tree(0.6*f_length, min_length)
        turtle.right(90)
        tree(0.6*f_length, min_length)
        turtle.left(45)
    turtle.back(f_length)

turtle.speed(50)
turtle.left(90)
tree(150)
turtle.mainloop()