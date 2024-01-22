"""
Teaching Fellow - Imperial College Dept of Computing - Interview Technical Exercise: Turtle Graphics Implementation in Python

This module provides a simple implementation of Turtle Graphics.
It offers a Turtle class that simulates a turtle moving around the canvas, drawing as it goes.
Users can control the turtle's movement, color, and pen state to create various geometric shapes and patterns.

Classes:
    Turtle: Represents a turtle in the Turtle Graphics system. It can move forward and backward, turn left and right, lift or put down its pen, and draw circles.

Usage:
    from turtle_graphics.turtle import Turtle
    t = Turtle()
    t.forward(100)
    t.right(90)
    # ... more turtle actions ...

Dependencies:
    - matplotlib: Used for rendering the graphical representation of the Turtle's and its path.
    - math: Provides mathematical functions for calculations.
    - config: Provides the canvas size limits.

Note:
    This implementation is designed for educational purposes and may not cover all features found in standard Turtle Graphics libraries.

Author: Leonardo Alves Dias
Version: 0.1
License: This project is open-source and free to use. You are permitted to use, modify, distribute, and perform the software for any purpose, including commercial applications, with no restrictions.
"""

import matplotlib.pyplot as plt
import math
from .config import SCREEN_LIMIT_X, SCREEN_LIMIT_Y

class Turtle:
    """Represents a turtle in a turtle graphics system.
    Attributes:
        name (str): Name of the turtle.
        x (float): X-coordinate of the turtle's current position.
        y (float): Y-coordinate of the turtle's current position.
        angle (float): Current direction of the turtle in degrees.
        is_pen_down (bool): State of the pen. True if down.
        line_color (str): Color of the line the turtle draws.
        turtle_color (str): Color of the turtle's symbol.
        line_thickness (float): Thickness of the line the turtle draws.
        lines_to_draw (List[tuple[tuple[float, float], tuple[float, float], str, float]]): List of lines to draw, each represented as a tuple containing start and end coordinates, color, and thickness.
    """
    def __init__(self, name: str = "Turtle", x: float = 0, y: float = 0,
                 init_angle: float = 90, line_color: str = 'black',
                 turtle_color: str = 'green') -> None:
        """Initialize the Turtle with a name, position, angle, and colors."""
        self.name = name
        self.x, self.y = x, y               #start in the canvas centre by default as (x,y) = (0,0)
        self.angle = init_angle             #start facing the north of the canvas by default as init_angle = 90
        self.is_pen_down = True
        self.line_color = line_color        #default line colour: black
        self.turtle_color = turtle_color    #default turtle colour: green
        self.line_thickness = 1
        self.lines_to_draw = []


    # Turtle moves
    def forward(self, distance: float) -> None:
        """Move the turtle forward by a specified distance.
        Args:
            distance (float): The distance to move backward.        
        Raises:
            TypeError: If the distance is not a number.
        """
        if not isinstance(distance, (int, float)):
            raise TypeError(f"Invalid type for distance: {type(distance).__name__}. Expected a number.")
        
        # Calculate new position
        new_x = self.x + distance * math.cos(math.radians(self.angle))
        new_y = self.y + distance * math.sin(math.radians(self.angle))

        if self.is_pen_down:
            self.lines_to_draw.append(((self.x, self.y), (new_x, new_y), self.line_color, self.line_thickness))
        self.x, self.y = new_x, new_y

        if not (-SCREEN_LIMIT_X <= self.x <= SCREEN_LIMIT_X and -SCREEN_LIMIT_Y <= self.y <= SCREEN_LIMIT_Y):
            raise ValueError(f"Turtle {self.name} has moved outside the screen limits ({-SCREEN_LIMIT_X}, {-SCREEN_LIMIT_Y}, {SCREEN_LIMIT_X}, {SCREEN_LIMIT_Y}).")


    def backward(self, distance: float) -> None:
        """Move the turtle backward by a specified distance.
        Args:
            distance (float): The distance to move backward.        
        Raises:
            TypeError: If the distance is not a number.
        """
        if not isinstance(distance, (int, float)):
            raise TypeError(f"Invalid type for distance: {type(distance).__name__}. Expected a number.")
        
        self.forward(-distance)


    def right(self, angle: float) -> None:
        """Turn the turtle to the right by a specified angle.
        Args:
            angle (float): The angle in degrees to turn the turtle to the right.
        Raises:
            TypeError: If the angle is not a number.
        """
        if not isinstance(angle, (int, float)):
            raise TypeError(f"Invalid type for angle: {type(angle).__name__}. Expected a number.")
        
        self.angle -= angle
        self.angle %= 360   #Ensures the angle is always between 0-359


    def left(self, angle: float) -> None:
        """Turn the turtle to the left by a specified angle.
        Args:
            angle (float): The angle in degrees to turn the turtle to the left.
        Raises:
            TypeError: If the angle is not a number.
        """
        if not isinstance(angle, (int, float)):
            raise TypeError(f"Invalid type for angle: {type(angle).__name__}. Expected a number.")
        
        self.angle += angle
        self.angle %= 360

    
    def circle(self, radius: float, extent: float = 360) -> None:
        """Draw a circle with a given radius and extent by approximating it with line segments.
        Args:
            radius (float): The radius of the circle.
            extent (float): The extent of the circle in degrees. Default is 360 for a full circle.
        Raises:
            TypeError: If the radius is not a number.
        Note:
            The formula used steps = int(2 * math.pi * radius / 10) is an approach to approximate circles using line segments.
            Reducing the value, e.g., from 10 to 5, increases smoothness as more lines are added to the circle. But it requires more rendering/processing time.
            Increasing the value, e.g., from 10 to 20, decreases smoothness as less lines are added to the circle. But it requires less rendering/processing time.
            For more information read: https://www.mathopenref.com/coordcirclealgorithm.html
        """
        if not isinstance(radius, (int, float)):
            raise TypeError(f"Invalid type for radius: {type(radius).__name__}. Expected a number.")
       
        # Number of steps depends on the circle's size for smoothness
        steps = int(2 * math.pi * radius / 10)
        step_length = 2 * math.pi * radius / steps
        step_angle = extent / steps
        for _ in range(steps):
            self.forward(step_length)
            self.right(step_angle)


    #Turtle controls
    def pen_up(self) -> None:
        """Lift the pen up. No line will be drawn when the turtle moves."""
        self.is_pen_down = False    #Stops appending lines to self.lines_to_draw list


    def pen_down(self) -> None:
        """Put the pen down. The turtle will draw lines when it moves."""
        self.is_pen_down = True     #Enables appending lines to self.lines_to_draw list


    def set_initial_angle(self, angle: float) -> None:
        """Set the initial angle of the turtle.
        Args:
            angle (float): The initial angle in degrees.
        Raises:
            TypeError: If the angle is not a number.
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Angle must be a number.")
        
        self.angle = angle
 

    def goto(self, x: float, y: float) -> None:
        """Move the turtle to a specific set of coordinates.
        Args:
            x (float): The x-coordinate to move to.
            y (float): The y-coordinate to move to.
        Raises:
            TypeError: If the coordinates are not numbers.
            ValueError: If the coordinates are outside the screen limits.
        """
        if x is None or y is None:
            x, y = 0, 0  # Default position (0, 0)
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"Invalid coordinate types: x is {type(x).__name__}, y is {type(y).__name__}. Expected numbers.")        
        if not (-SCREEN_LIMIT_X <= x <= SCREEN_LIMIT_X and -SCREEN_LIMIT_Y <= y <= SCREEN_LIMIT_Y):
            raise ValueError(f"Coordinates ({x}, {y}) are outside the screen limits ({-SCREEN_LIMIT_X}, {-SCREEN_LIMIT_Y}, {SCREEN_LIMIT_X}, {SCREEN_LIMIT_Y}).")
        
        if self.is_pen_down:
            # Draw a line to the new position if the pen is down
            self.lines_to_draw.append(((self.x, self.y), (x, y), self.line_color, self.line_thickness))
        
        # Update the turtle's position
        self.x, self.y = x, y


    def reset(self) -> None:
        """Reset the turtle to its initial state."""
        self.x = 0
        self.y = 0
        self.angle = 90
        self.is_pen_down = True
        self.line_color = 'black'
        self.turtle_color = 'green'
        self.line_thickness = 1
        self.lines_to_draw.clear()
    

    def get_position(self) -> tuple[float, float]:
        """Get the current position of the turtle.
        Returns:
            tuple[float, float]: The current (x, y) coordinates of the turtle.
        """
        return self.x, self.y
    

    def get_drawing_data(self) -> list[tuple[tuple[float, float], tuple[float, float], str, float]]:
        """Get the data for lines drawn by the turtle.
        Returns:
            list[tuple[tuple[float, float], tuple[float, float], str, float]]: 
                A list of tuples representing the lines drawn. Each tuple contains start and end coordinates, line color, and line thickness.
        """
        return self.lines_to_draw
    

    # Turtle properties   
    def set_pen_color(self, color: str) -> None:
        """Set the colour of the pen.
        Args:
            colour (str): The colour to set the pen to.
        Raises:
            TypeError: If the colour is not a string.
        """
        if not isinstance(color, str):
            raise TypeError("Line colour must be a string.")
        
        self.line_color = color
    

    def set_turtle_color(self, color: str) -> None:
        """Set the colour of the turtle symbol.
        Args:
            colour (str): The colour to set the turtle symbol to.
        Raises:
            TypeError: If the colour is not a string.
        """
        if not isinstance(color, str):
            raise TypeError("Turtle colour must be a string.")
        
        self.turtle_color = color
    
    
    def set_line_thickness(self, thickness: float) -> None:
        """Set the thickness of the line the turtle draws.
        Args:
            thickness (float): The thickness of the line.
        Raises:
            TypeError: If the thickness is not a number.
        """
        if not isinstance(thickness, (int, float)):
            raise TypeError("Line thickness must be a number.")
        
        self.line_thickness = thickness