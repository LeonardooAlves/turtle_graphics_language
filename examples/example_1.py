# Import the Turtle class and the draw_all_turtles function
from turtle_graphics.turtle import Turtle
from turtle_graphics.drawing import draw_all_turtles

def main():
    # Create a new Turtle instance
    my_turtle = Turtle()

    # Set up turtle properties (optional)
    my_turtle.set_pen_color('blue')
    my_turtle.set_line_thickness(2)

    # Move the turtle to draw a square
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)

    # Display the path of the turtle
    draw_all_turtles("My Turtle Drawing", my_turtle)

if __name__ == "__main__":
    main()
