from turtle import Turtle, Screen
import random

# set the size of main window
screen = Screen()
screen.setup(width=500, height=400)


def set_turtle_args(turtle_object, color_text, x_coordinate, y_coordinate):
    """Sets the color and initial position of turtle object."""
    turtle_object.color(color_text)
    turtle_object.penup()
    turtle_object.goto(x=x_coordinate, y=y_coordinate)


def add_new_turtle(turtles_list):
    """Creates a new turtle object and add the turtle object to an input list"""
    turtle_obj = Turtle(shape="turtle")
    turtles_list.append(turtle_obj)


# ask user for the bet
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a rainbow color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
while user_bet not in colors:
    user_bet = screen.textinput("Make your bet", f"Invalid input. Choose between {'/'.join(colors)}: ").lower()
turtles = []

# set initial coordinates and gap between turtles
x = -230
y = 130
gap_turtle = 50

# create the turtles and set the arguments
for index_turtle in range(6):
    add_new_turtle(turtles)
    set_turtle_args(turtles[index_turtle], colors[index_turtle], x, y - gap_turtle * index_turtle)

end_of_race = False
finish_line_y = screen.window_width()/2 - 10
while not end_of_race:
    for race_turtle in turtles:
        random_distance = random.randint(1, 10)
        race_turtle.forward(random_distance)
        # verify if race_turtle y coordinate is equal to finish line y coordinate
        if race_turtle.position()[0] > finish_line_y:
            end_of_race = True
            winner_turtle = race_turtle
            break

# keep only the winner turtle on the screen
for turtle in turtles:
    if not turtle == winner_turtle:
        turtle.hideturtle()
    else:
        winner_turtle.goto(0, 0)

# set title window for info user
if winner_turtle.pencolor() == user_bet:
    screen.title(f"You've won! The {winner_turtle.pencolor()} turtle is the winner!")
else:
    screen.title(f"You've lost! The {winner_turtle.pencolor()} turtle is the winner!")

screen.exitonclick()
