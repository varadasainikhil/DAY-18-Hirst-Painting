import turtle as t
import random
import colorgram
t.colormode(255)

# To generate the color palette from any image
colors = colorgram.extract('Spot-Painting-Image.jpg', 20)
final_color = []

for i in range(len(colors)):
    x = colors[i]
    r = x.rgb.r
    g = x.rgb.g
    b = x.rgb.b
    new_color = (r, g, b)
    final_color.append(new_color)

# Global Parameters
dot_size = 30
gap_between_lines = 60
size_of_square = 10
down = 270
right = 0
left = 180
up = 90

# To calculate the starting point
start_point = (gap_between_lines * size_of_square)/2

turtle = t.Turtle()
screen = t.Screen()
turtle.speed("fastest")
turtle.hideturtle()

# To center the painting
turtle.penup()
turtle.setheading(left)
turtle.forward(start_point)
turtle.setheading(up)
turtle.forward(start_point)
turtle.setheading(0)
for j in range(1, size_of_square + 1):
    for i in range(size_of_square):
        turtle.dot(dot_size, random.choice(final_color))
        turtle.penup()
        turtle.forward(gap_between_lines)
    if j % 2 == 0:
        turtle.setheading(down)
        turtle.forward(gap_between_lines)
        turtle.setheading(right)
        turtle.forward(gap_between_lines)
    else:
        turtle.setheading(down)
        turtle.forward(gap_between_lines)
        turtle.setheading(left)
        turtle.forward(gap_between_lines)
screen.exitonclick()
