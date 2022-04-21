from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)  # debug
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtle(obj, color, x_pos, y_pos):
    obj = Turtle(shape="turtle")
    obj.color(color)
    obj.penup()
    obj.goto(x=x_pos, y=y_pos)
    return obj


t1 = create_turtle(obj="t1", color=colors[0], x_pos=-230, y_pos=-20)
t2 = create_turtle(obj="t2", color=colors[1], x_pos=-230, y_pos=-70)
t3 = create_turtle(obj="t3", color=colors[2], x_pos=-230, y_pos=-120)
t4 = create_turtle(obj="t4", color=colors[3], x_pos=-230, y_pos=30)
t5 = create_turtle(obj="t5", color=colors[4], x_pos=-230, y_pos=80)
t6 = create_turtle(obj="t6", color=colors[5], x_pos=-230, y_pos=130)


screen.exitonclick()
