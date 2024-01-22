# Import the Turtle class and the draw_all_turtles function
from turtle_graphics.turtle import Turtle
from turtle_graphics.drawing import draw_all_turtles

def main():
    # Create a new Turtle instance
    my_turtle = Turtle()

    # Set up turtle properties (optional)
    my_turtle.set_pen_color('blue')

    #Draw different (four) circles of different radius with the same starting point. The circles also have a different line thickness.    
    num_circles=10
    circle_line_thickness = 1
    while num_circles <= 40:
        my_turtle.set_line_thickness(circle_line_thickness)
        my_turtle.circle(num_circles)
        num_circles+=10
        circle_line_thickness+=1

    # Display the path of the turtle
    draw_all_turtles("Six Circles Drawing", my_turtle)

if __name__ == "__main__":
    main()
