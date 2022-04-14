import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the states!")
screen.setup(725, 491)  # window size is the same as the dimensions of the states image

bg = "blank_states_img.gif"
screen.addshape(bg)
turtle.shape(bg)

data = pandas.read_csv("50_states.csv").values.tolist()
used_states = []
score = 0

while True:
    state = turtle.textinput(title=f"{score}/50", prompt="Guess the name of a state")

    if state == "quit":
        screen.bye()

    for row in data:
        if row[0].lower() == state and state not in used_states:
            x, y = row[1], row[2]
            score += 1

            state_label = turtle.Turtle()
            state_label.penup()
            state_label.ht()
            state_label.goto(x, y)
            state_label.write(f"{state}", font=("Verdana", 8, "normal"))

            used_states.append(state)
