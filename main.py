from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
game_running = True
user_bet = screen.textinput(title="Make your bet", prompt="Choose your turtle's color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = -100
turtle_list = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, position)
    position += 35
    turtle_list.append(new_turtle)

while game_running:
    for turtle in turtle_list:
        rng = random.randint(0, 10)
        turtle.forward(rng)
        if turtle.xcor() > 225:
            game_running = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You Won! The {winning_turtle} turtle won!")
            else:
                print(f"You lost. The {winning_turtle} turtle won!")








screen.exitonclick()