import unittest
from turtle_graphics.turtle import Turtle
from turtle_graphics.config import SCREEN_LIMIT_X, SCREEN_LIMIT_Y

class TestTurtle(unittest.TestCase):
    """Tests for the Turtle class."""

    def setUp(self):
        """Create a new Turtle object for each test."""
        self.turtle = Turtle()

    def test_initial_position_and_angle(self):
        """Test the initial position and angle of the Turtle."""
        self.assertEqual(self.turtle.x, 0)
        self.assertEqual(self.turtle.y, 0)
        self.assertEqual(self.turtle.angle, 90)

    def test_forward_movement(self):
        """Test the turtle's forward movement."""
        self.turtle.forward(100)
        self.assertNotEqual(self.turtle.x, 0)
        self.assertNotEqual(self.turtle.y, 0)

    def test_backward_movement(self):
        """Test the turtle's backward movement."""
        initial_position = (self.turtle.x, self.turtle.y)
        self.turtle.backward(100)
        self.assertNotEqual((self.turtle.x, self.turtle.y), initial_position)

    def test_right_turn(self):
        """Test turning the turtle to the right."""
        initial_angle = self.turtle.angle
        self.turtle.right(90)
        self.assertNotEqual(self.turtle.angle, initial_angle)

    def test_left_turn(self):
        """Test turning the turtle to the left."""
        initial_angle = self.turtle.angle
        self.turtle.left(90)
        self.assertNotEqual(self.turtle.angle, initial_angle)

    def test_pen_up_down(self):
        """Test lifting and dropping the pen."""
        self.turtle.pen_up()
        self.assertFalse(self.turtle.is_pen_down)
        self.turtle.pen_down()
        self.assertTrue(self.turtle.is_pen_down)

    def test_invalid_forward_distance(self):
        """Test forward movement with invalid distance."""
        with self.assertRaises(TypeError):
            self.turtle.forward("not_a_number")

    def test_invalid_backward_distance(self):
        """Test backward movement with invalid distance."""
        with self.assertRaises(TypeError):
            self.turtle.backward("not_a_number")

    def test_invalid_right_angle(self):
        """Test right turn with invalid angle."""
        with self.assertRaises(TypeError):
            self.turtle.right("not_a_number")

    def test_invalid_left_angle(self):
        """Test left turn with invalid angle."""
        with self.assertRaises(TypeError):
            self.turtle.left("not_a_number")

    def test_boundary_check(self):
        """Test if the turtle stops at the screen boundary."""
        with self.assertRaises(ValueError):
            self.turtle.goto(SCREEN_LIMIT_X + 1, SCREEN_LIMIT_Y + 1)

    def test_goto(self):
        """Test the turtle's ability to go to a specific position."""
        self.turtle.goto(50, 75)
        self.assertEqual((self.turtle.x, self.turtle.y), (50, 75))

    def test_reset(self):
        """Test the turtle's ability to reset its state."""
        self.turtle.forward(100)
        self.turtle.right(90)
        self.turtle.set_pen_color('red')
        self.turtle.set_line_thickness(3)
        self.turtle.reset()
        self.assertEqual((self.turtle.x, self.turtle.y), (0, 0))
        self.assertEqual(self.turtle.angle, 90)
        self.assertEqual(self.turtle.line_color, 'black')
        self.assertEqual(self.turtle.line_thickness, 1)
        self.assertTrue(self.turtle.is_pen_down)

    def test_set_pen_color(self):
        """Test setting the pen color."""
        self.turtle.set_pen_color('blue')
        self.assertEqual(self.turtle.line_color, 'blue')

    def test_set_turtle_color(self):
        """Test setting the turtle color."""
        self.turtle.set_turtle_color('green')
        self.assertEqual(self.turtle.turtle_color, 'green')

    def test_set_line_thickness(self):
        """Test setting the line thickness."""
        self.turtle.set_line_thickness(5)
        self.assertEqual(self.turtle.line_thickness, 5)


if __name__ == "__main__":
    unittest.main()
