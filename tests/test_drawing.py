import unittest
from turtle_graphics.turtle import Turtle
from turtle_graphics.drawing import draw_all_turtles
from unittest.mock import patch
import matplotlib.pyplot as plt

class TestDrawing(unittest.TestCase):
    """Tests for the drawing functionality in the Turtle Graphics system."""

    def test_draw_all_turtles_with_single_turtle(self):
        """Test drawing a single Turtle object."""
        turtle = Turtle()
        turtle.forward(100)

        # Mock plt.show to prevent actually displaying the plot during testing
        with patch.object(plt, 'show'):
            draw_all_turtles(turtle)

    def test_draw_all_turtles_with_multiple_turtles(self):
        """Test drawing multiple Turtle objects."""
        turtle1 = Turtle()
        turtle2 = Turtle()

        turtle1.forward(100)
        turtle2.left(90)
        turtle2.forward(100)

        with patch.object(plt, 'show'):
            draw_all_turtles(turtle1, turtle2)

    def test_draw_all_turtles_with_title(self):
        """Test drawing with a custom title."""
        turtle = Turtle()
        turtle.forward(100)
        custom_title = "Custom Title"

        with patch.object(plt, 'show'):
            draw_all_turtles(custom_title, turtle)

        # Check if the title is set correctly
        self.assertEqual(plt.gca().get_title(), custom_title)

if __name__ == "__main__":
    unittest.main()
