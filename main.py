import turtle
from turtle import Turtle, Screen
import random

# tom = Turtle("turtle")
screen = Screen()

user = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color : ")
color = ["red", "blue", "green", "pink", "yellow", "violet"]
position = -150
alltim = []
for i in range(0, 6):
    tim = Turtle("turtle")
    tim.penup()
    tim.color(color[i])
    tim.goto(-470, position)
    position += 50
    alltim.append(tim)
if user:
    israceon = True

while israceon:
    for tim in alltim:
        if tim.xcor() > 451:
            israceon = False
            winner = tim.pencolor()
            if winner == user:
                print(f"You've won! The {winner} turtle is the winner")
            else:
                print(f"You've lost! The {winner} turtle is the winner")
        tim.forward(random.randint(10, 30))
screen.exitonclick()
