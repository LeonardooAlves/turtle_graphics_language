# Import the Turtle class and the draw_all_turtles function
from turtle_graphics.turtle import Turtle
from turtle_graphics.drawing import draw_all_turtles

def draw_polygon(turtle, sides, size):
    """Draw a regular polygon with given sides and size."""
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(size)
        turtle.right(angle)

def draw_circle(turtle, radius):
    """Draw a circle with the given radius."""
    turtle.circle(radius)

def draw_diamond(turtle, size):
    """Draw a diamond shape."""
    for _ in range(2):
        turtle.forward(size)
        turtle.right(60)
        turtle.forward(size)
        turtle.right(120)

def main():
    # Create a new Turtle instance
    polygon_turtle = Turtle()
    circle_turtle = Turtle()
    diamond_turtle = Turtle()

    # Set up turtle properties (optional)
    polygon_turtle.set_pen_color('red')
    circle_turtle.set_pen_color('green')
    circle_turtle.set_initial_angle(90)
    diamond_turtle.set_pen_color('blue')

    # Draw a polygon
    draw_polygon(polygon_turtle, 5, 70)  # Pentagon

    # Draw a cricle    
    draw_circle(circle_turtle, 50)

    # Draw a diamond  
    draw_diamond(diamond_turtle, 100)

    # Display the path of the turtle
    draw_all_turtles("Three Different Shapes", polygon_turtle, circle_turtle, diamond_turtle)

if __name__ == "__main__":
    main()
