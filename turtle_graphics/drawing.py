"""
Teaching Fellow - Imperial College Dept of Computing - Interview Technical Exercise:

Drawing functionality for Turtle Graphics Implementation in Python

This module provides functions to draw the Turtles' symbrol representation and paths created by their objects. 
It includes the draw_all_turtles function, which takes multiple Turtle objects and 
displays their paths on a single matplotlib plot.

Functions:
    draw_symbol()
    draw_all_turtles(*args): Draws the paths of all provided Turtle instances on a matplotlib plot.

Example:
    from turtle_graphics.turtle import Turtle
    from turtle_graphics.drawing import draw_all_turtles

    t = Turtle()
    t.forward(100)
    draw_all_turtles("Example Drawing", t)

Dependencies:
    - matplotlib: Used for rendering the graphical representation of the Turtle's and its path.
    - math: Provides mathematical functions for calculations.
    - config: Provides the canvas size limits.

Author: Leonardo Alves Dias
Version: 0.1
License: This project is open-source and free to use. You are permitted to use, modify, distribute, and perform the software for any purpose, including commercial applications, with no restrictions.
"""

import matplotlib.pyplot as plt
import math
from .config import SCREEN_LIMIT_X, SCREEN_LIMIT_Y

def draw_symbol(turtle, ax) -> None:
    """Draw the symbol representing the turtle on the given axes.
    Args:
        turtle: the turtle object to be represented via a symbol.
        ax: The matplotlib axes to draw on.
    """
    # Draw a simple triangle to represent the turtle
    size = 5  # Size of the symbol
    angle_rad = math.radians(turtle.angle)
    # Calculate the vertices of the triangle
    vertices = [
        (turtle.x + size * math.cos(angle_rad), turtle.y + size * math.sin(angle_rad)),
        (turtle.x + size * math.cos(angle_rad + 2.0 * math.pi / 3), turtle.y + size * math.sin(angle_rad + 2.0 * math.pi / 3)),
        (turtle.x + size * math.cos(angle_rad + 4.0 * math.pi / 3), turtle.y + size * math.sin(angle_rad + 4.0 * math.pi / 3))
    ]
    triangle = plt.Polygon(vertices, color=turtle.turtle_color)
    ax.add_patch(triangle)

def draw_all_turtles(*args) -> None:
    """
    Draw all provided turtles on a matplotlib plot.
    This function takes an optional title followed by multiple Turtle objects,
    retrieves the lines and symbols they have drawn, and displays them on a single
    matplotlib plot.
    Args:
        args: A list that may start with a title (str) followed by Turtle objects.
    Note:
        If no title is provided, "Turtle Drawing" is used as the default title.
        The function sets the plot limits to (-SCREEN_LIMIT, SCREEN_LIMIT) for both x and y axes,
        assuming these as screen limits for the Turtle graphics.
    """
    title = "Turtle Drawing"
    turtles_start_index = 0

    if args and isinstance(args[0], str):
        title = args[0]
        turtles_start_index = 1

    plt.figure()
    plt.title(title)
    ax = plt.gca()
    for turtle in args[turtles_start_index:]:
        set_of_lines = turtle.get_drawing_data()
        for line in set_of_lines:
            start, end, color, thickness = line
            plt.plot([start[0], end[0]], [start[1], end[1]], color=color, linewidth=thickness)
        draw_symbol(turtle, ax)

    plt.xlim(-SCREEN_LIMIT_X, SCREEN_LIMIT_X)
    plt.ylim(-SCREEN_LIMIT_Y, SCREEN_LIMIT_Y)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()