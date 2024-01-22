# Import the Turtle class and the draw_all_turtles function
from turtle_graphics.turtle import Turtle
from turtle_graphics.drawing import draw_all_turtles

def draw_koch_segment(turtle, length, depth):
    """
    Recursively draw a segment of the Koch snowflake.
    This function divides the segment into smaller parts and applies the Koch snowflake construction rules at each recursion level.
    Args:
        turtle (Turtle): The turtle object used for drawing.
        length (float): The length of the Koch segment.
        depth (int): The recursion depth. When depth is 0, a straight line is drawn.
    The Koch construction rule:
    - Divide the line segment into three segments of equal length.
    - Draw an equilateral triangle that has the middle segment from step 1 as its base,
      and remove the line that was the base of the triangle.
    - Repeat the process for each of the four new line segments.
    """
    if depth == 0:
        # Base case: simply draw a straight line
        turtle.forward(length)
    else:
        # Recursive case: divide the line and apply Koch construction rules.
        # The combination of these moves results in a single Koch snowflake segment.
        length /= 3.0

        # Draw the first segment
        draw_koch_segment(turtle, length, depth-1)

        # Turn left and draw the second segment (the first side of the triangle)
        turtle.left(60)
        draw_koch_segment(turtle, length, depth-1)

        # Turn right and draw the third segment (the base of the triangle is skipped)
        turtle.right(120)
        draw_koch_segment(turtle, length, depth-1)

        # Turn left again and draw the fourth segment (the second side of the triangle)
        turtle.left(60)
        draw_koch_segment(turtle, length, depth-1)

def draw_koch_snowflake(turtle, length, depth):
    """Draw a Koch snowflake."""
    for _ in range(3):
        draw_koch_segment(turtle, length, depth)
        turtle.right(120)

def main():
    # Create a new Turtle instance
    snowflake_turtle = Turtle()

    # Set up turtle properties (optional)
    snowflake_turtle.set_pen_color('blue')

    # Define the size and depth of the Koch snowflake
    size = 100
    depth = 3

    # Draw the Koch snowflake
    draw_koch_snowflake(snowflake_turtle, size, depth)

    # Display the path of the turtle
    draw_all_turtles("Single Koch Snowflake", snowflake_turtle)

if __name__ == "__main__":
    main()
