from turtle import Turtle, Screen
# import turtle as t
# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

# ####### Challenge 1 - Draw a Square ############
tim = Turtle()
tim.shape("turtle")
tim.color("DodgerBlue")

for _ in range(4):
    tim.right(90)
    tim.forward(100)

# ### draw a dashed line
tom = Turtle()
for _ in range(15):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()
