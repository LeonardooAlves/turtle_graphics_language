# Import the Turtle class and the draw_all_turtles function
from turtle_graphics.turtle import Turtle
from turtle_graphics.drawing import draw_all_turtles

def draw_square(turtle, size):
    """Draw a square with the given size."""
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

def draw_triangle(turtle, size):
    """Draw an equilateral triangle with the given size."""
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

def main():
    # Create a new Turtle instance
    house_turtle = Turtle()

    # Set up turtle properties (optional)
    house_turtle.set_pen_color('brown')
    house_turtle.set_line_thickness(2)

    # Draw a square
    draw_square(house_turtle, 100)

    # Draw a triangle above the square to resemble a house
    house_turtle.pen_up()
    house_turtle.forward(100)
    house_turtle.right(90)
    house_turtle.pen_down()
    draw_triangle(house_turtle, 100)

    # Display the path of the turtle
    draw_all_turtles("Simple House", house_turtle)

if __name__ == "__main__":
    main()
