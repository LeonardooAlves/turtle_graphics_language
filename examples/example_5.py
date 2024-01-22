# Import the Turtle class and the draw_all_turtles function
from turtle_graphics.turtle import Turtle
from turtle_graphics.drawing import draw_all_turtles

def draw_sierpinski(turtle, order, size):
    """
    Recursively draw a Sierpinski triangle of a given order and size.
    The Sierpinski triangle is a fractal and attractive fixed set with the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles.
    Args:
        turtle (Turtle): The turtle object used for drawing.
        order (int): The recursion depth, which determines the level of detail in the triangle.
        size (float): The length of the sides of the outermost triangle.
    The Sierpinski construction rule:
    - At the base case (order 0), draw an equilateral triangle.
    - For higher orders, divide the triangle into three smaller triangles and
      recursively apply the same process to each smaller triangle.
    """
    if order == 0:
        # Base case: draw an equilateral triangle
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        # Recursive case: divide the triangle and apply the rule to each part.
        # The recursive process creates the characteristic pattern of the Sierpinski triangle
        draw_sierpinski(turtle, order-1, size/2)
        turtle.forward(size/2)
        draw_sierpinski(turtle, order-1, size/2)
        turtle.backward(size/2)
        turtle.left(60)
        turtle.forward(size/2)
        turtle.right(60)
        draw_sierpinski(turtle, order-1, size/2)
        turtle.left(60)
        turtle.backward(size/2)
        turtle.right(60)       


def main():
    # Create a new Turtle instance
    sierpinski_turtle = Turtle()

    # Set up turtle properties (optional)
    sierpinski_turtle.set_pen_color('purple')

    # Define the size and order of the Sierpinski triangle
    size = 150
    order = 3
    
    # Draw the Sierpinski triangle
    draw_sierpinski(sierpinski_turtle, order, size)

    # Display the path of the turtle
    draw_all_turtles("Single Sierpinski Triangle", sierpinski_turtle)

if __name__ == "__main__":
    main()
