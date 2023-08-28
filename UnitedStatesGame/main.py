import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=525)
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


def mouse_click_state_coord(x, y):
    print(x, y)


turtle.onscreenclick(mouse_click_state_coord)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_Learn.csv")
        break

    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_answer = data[data.state == answer]
        x_cord = int(state_answer.x)
        y_cord = int(state_answer.y)
        t.goto(x_cord, y_cord)
        t.write(answer)

turtle.mainloop()
