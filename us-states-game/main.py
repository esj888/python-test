# 1. convert the guess to Title case
# 2. check if the guess is among the 50 states
# 3. write correct guesses onto map
# 4. use a loop to allow the user to keep guessing
# 5. record the correct guesses in a list
# 6. keep track of the score
# 7. write states_to_learn.csv with states that were missed

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

no_of_guesses = 0
no_of_correct = 0
all_states = pandas.read_csv("50_states.csv")
states = all_states["state"]

# testing deleting row
# del_idx = states[states == "Hawaii"].index
# missed_states = states.drop(del_idx)
# print(missed_states)


def write_state(name_of_state):
    print(name_of_state)      # debug
    print_state = all_states[all_states.state == name_of_state]
    state_x = int(print_state.x)
    state_y = int(print_state.y)
    print(state_x, state_y)

    # print(print_state.state.str.len())
    state_list = print_state.state.values.tolist()         # convert df to list
    state_text = state_list[0]                             # print first item

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(state_x, state_y)
    t.pendown()
    t.write(state_text)


for x in range(50):
    print("start loop")
    answer_state = screen.textinput(title=f"{no_of_correct}/50 States Correct", prompt="What's another State's name?")
    no_of_guesses += 1
    if answer_state == "quit":
        print("quitting")
        break

    # test_str = "Florida"         # testing
    # print(states)
    # print(states["state"])

    # checking if answer is correct
    correct = False
    for state in states:
        # print(state.lower())
        # print(answer_state.lower())
        if answer_state.lower() == state.lower():
            correct = True
            no_of_correct += 1
            # print(state)          # debug
            # write_state("Texas")  # ******************* debug manual works
            # write_state(test_str) # debug
            write_state(state)
            del_idx = states[states == state].index
            states = states.drop(del_idx)  # remove correct state

            # write_state(name_of_state=answer_state.lower()) # error ***********************
            # print(type(answer_state.lower()))
            # print(type("Texas"))
            # break # not looping 2nd time
        # else:
            # correct = False

    # print(correct)
    # if correct is True:
    #     no_of_correct += 1
    # print(no_of_correct)

    # def get_mouse_click_coor(x, y):
    #     print(x, y)
    #
    #
    # turtle.onscreenclick(get_mouse_click_coor)

    # testing writing Hawaii at location
    # t = turtle.Turtle()
    # t.hideturtle()
    # t.penup()
    # t.goto(-317, -143)
    # t.pendown()
    # t.write("Hawaii")

# turtle.mainloop()
# screen.exitonclick()         # needed to be outside the loop
print(states)
states.to_csv("states_to_learn.csv")

