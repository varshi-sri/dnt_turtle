import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the speed of the turtle
my_turtle.speed(1)

# Move the turtle to the starting position
my_turtle.penup()
my_turtle.goto(-100, 0)
my_turtle.pendown()

my_turtle.forward(70)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(70)
my_turtle.right(90)
my_turtle.forward(100)

# Move the turtle to the next letter
my_turtle.penup()
my_turtle.goto(0, -100)
my_turtle.pendown()

# Draw the letter N
my_turtle.forward(100)
my_turtle.right(135)
my_turtle.forward(141)
my_turtle.left(135)
my_turtle.forward(100)

# Move the turtle to the next letter
my_turtle.penup()
my_turtle.goto(130, 0)
my_turtle.pendown()

# Draw the letter T
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.left(180)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(100)

# Hide the turtle
my_turtle.hideturtle()

# Exit the turtle graphics window
turtle.done() 