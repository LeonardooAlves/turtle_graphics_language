"""
Teaching Fellow - Imperial College Dept of Computing - Interview Technical Exercise:

Interview Technical Exercise
 
This code implements the example request for this interview

Candidate: Leonardo Alves Dias (leonardoalves.tai@gmail.com)
"""

# Import the Turtle class and the draw_all_turtles function
from turtle_graphics.turtle import Turtle
from turtle_graphics.drawing import draw_all_turtles

def main():
    # Create a new Turtle instance
    tom = Turtle()

    # Set up turtle properties
    tom.set_pen_color("red")

    # Draw a square
    tom.forward(50)
    tom.left(90)
    tom.forward(50)
    tom.left(90)
    tom.forward(50)
    tom.left(90)
    tom.forward(50)

    # Display the path of the turtle
    draw_all_turtles("Interview Technical Exercise", tom)

if __name__ == "__main__":
    main()
