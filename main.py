import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
num_states_correct = 0

while (num_states_correct < 50):
    answer_state = screen.textinput(title=f"{num_states_correct}/50 States Correct", prompt="What's another state's name?")

    if answer_state in states:
        num_states_correct += 1
        a = turtle.Turtle()
        a.hideturtle()
        a.penup()
        xcor = data[data.state == answer_state].x
        ycor = data[data.state == answer_state].y
        a.goto(int(xcor), int(ycor))
        a.write(answer_state, font="Arial", align='center')

turtle.mainloop()