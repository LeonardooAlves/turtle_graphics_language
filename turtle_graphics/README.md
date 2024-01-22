# Turtle Graphics Function Overview

## `turtle.py`

`turtle.py` is a Python module that provides a `Turtle` class for the Turtle Graphics system. This class is designed to emulate a "turtle" that can move around a canvas, drawing as it goes.

To use this module, import it as `from turtle_graphics.turtle import Turtle`.

Notes:
- The turtle operates within a defined screen limit, and its position is calculated relative to a central point (0,0).
- Movements are calculated using trigonometric functions, considering the turtle's angle and the specified distance.
- Drawing functionalities utilize Python's [`matplotlib`](https://matplotlib.org/stable/) library for visual representation.

### `forward` method

1. **Type Check**: The method begins by checking if the `distance` parameter is a number (`int` or `float`). If not, it raises a `TypeError`.
   
2. **Calculate New Position**:
   - `new_x` and `new_y` calculate the turtle's new position after moving forward.
   - `math.cos(math.radians(self.angle))` and `math.sin(math.radians(self.angle))` are used to determine the x and y components, respectively, of the turtle's movement based on its current angle. The angle is first converted from degrees to radians, as the math module functions expect angles in radians.
   - The distance is multiplied with these components to determine how far the turtle moves along the x and y axes.

3. **Drawing the Line**: If the pen is down (`self.is_pen_down` is `True`), a line is drawn from the current position (`self.x`, `self.y`) to the new position (`new_x`, `new_y`) by appending a line to `self.lines_to_draw` along with its color and thickness.

4. **Update Position**:The turtle's position is updated to the new coordinates (`new_x`, `new_y`).

### `backward` method

Similar to `forward`, this method first checks if `distance` is a number. If not, a `TypeError` is raised. To move the turtle, it reuses the `forward` method by providing a negative `distance`. This effectively moves the turtle in the opposite direction of its current angle, simulating a backward movement.

Understanding the Direction (Angle): The angle is measured in degrees from the positive x-axis, typically in a counterclockwise direction. An angle of 0 degrees corresponds to facing right (east), 90 degrees is facing upwards (north), 180 degrees is left (west), and 270 degrees is downwards (south). `cos(θ)` and `sin(θ)` gives the horizontal and vertical components, respectively, of the movement for an angle `θ`.

### `circle` method

1. **Type Check**: The method starts by checking if the `radius` is a number (either `int` or `float`). If not, it raises a `TypeError`.

2. **Determining Steps**:`steps = int(2 * math.pi * radius / 10)` calculates the number of small linear segments to approximate the circle. The circle's circumference is `2 * math.pi * radius`. Dividing this by 10 (or another small number) gives an approximate number of steps needed to draw the circle. The choice of 10 as a divisor is a balance between performance (fewer steps) and accuracy (more steps).

3. **Calculating Step Length and Angle**:
   - `step_length = 2 * math.pi * radius / steps` calculates the length of each linear segment. It's essentially dividing the total circumference by the number of steps.
   - `step_angle = extent / steps` calculates the angle by which the turtle needs to turn after each step to create the circle. The `extent` parameter allows drawing only a portion of a circle. By default, it's 360 degrees, which means a full circle.

4. **Drawing the Circle**: The `for` loop iterates `steps` times. In each iteration, the turtle moves forward by `step_length` and then turns right by `step_angle`. This process creates a series of short, straight-line segments that approximate the curvature of a circle.

### `right` method

- **Type Check**: Validates that the `angle` argument is a number. If not, raises `TypeError`.

- **Angle Adjustment**: Subtracts the given `angle` from the turtle's current angle (`self.angle`). This simulates a right turn.

- **Modulo Operation**: Ensures the turtle's angle remains within the 0-359 degrees range using modulo 360.

### `left` method

Similar to the `right` method, it checks if `angle` is a number, otherwise, raises a `TypeError`, and ensures the angle is within 0-359 degrees using modulo 360. However, it adds the given `angle` to the turtle's current angle to represent a left turn.

### `goto` method

- **Default Position**: If `x` or `y` are `None`, the turtle is moved to the default position (0, 0).

- **Type Check**: Verifies that `x` and `y` are numerical values. If not, a `TypeError` is raised.

- **Boundary Check**: Ensures the new coordinates are within the defined screen limits. If they are outside these limits, a `ValueError` is raised.

- **Drawing Line**: If the pen is down (`self.is_pen_down` is `True`), a line is drawn from the current position to the new coordinates. This line, along with its color and thickness, is added to `self.lines_to_draw`.

- **Update Position**: The turtle's position is updated to the new coordinates (`x`, `y`).

## drawing.py

The `drawing.py` module is part of the Turtle Graphics Project, responsible for displaying the movements and drawings created by Turtle objects. It uses Matplotlib.

To use this module, import it as `from turtle_graphics.drawing import draw_all_turtles`, and call `draw_all_turtles` with Turtle instances to visualize their paths and current positions on a plot.

Notes:
- The function above assumes the screen limits defined in `.config.py` as the boundary for the plot. Thereofre, it sets the plot limits to (-SCREEN_LIMIT_X, SCREEN_LIMIT_X) and (-SCREEN_LIMIT_Y, SCREEN_LIMIT_Y) for the x and y axes, respectively.
- "Turtle Drawing" is used as the default title if none is provided.

### draw_symbol function

`draw_symbol` is a function that draws a symbol representing a turtle's current position and orientation on the given Matplotlib axes (`ax`). The symbol is typically a triangle, indicating the direction the turtle is facing.

#### Computational Thinking

- **Symbol Size**: `size = 5` sets the turtle's symbol size (triangle shape), determining how large it will appear on the plot.

- **Angle Conversion**: `angle_rad = math.radians(self.angle)` converts the turtle's current angle from degrees to radians. The `math.radians` function is used because trigonometric functions in Python's `math` module require angles in radians.

```python
    vertices = [
        (self.x + size * math.cos(angle_rad), self.y + size * math.sin(angle_rad)),
        (self.x + size * math.cos(angle_rad + 2.0 * math.pi / 3), self.y + size * math.sin(angle_rad + 2.0 * math.pi / 3)),
        (self.x + size * math.cos(angle_rad + 4.0 * math.pi / 3), self.y + size * math.sin(angle_rad + 4.0 * math.pi / 3))
    ]
```
- **Vertex definition**: A list named `vertices` is initialized to store the coordinates of the triangle's corners. The first vertex is defined by the trigonometric functions (`math.cos` and `math.sin`) to find the point `size` units away from the turtle's current position (`self.x`, `self.y`) in the direction it is facing (`angle_rad`). The second vertex is adjusted by adding `2.0 * math.pi / 3` radians (120 degrees) to `angle_rad`, creating an equilateral triangle. Similar to the second vertex, the third vertex is defined by adding `4.0 * math.pi / 3` radians (240 degrees) to `angle_rad`.

```python
    triangle = plt.Polygon(vertices, color=self.turtle_color)
```
- **Creating the Polygon**: Uses [Matplotlib's `Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html) class to create a triangle with the calculated vertices. The color of the triangle is set to `self.turtle_color`.

```python
    ax.add_patch(triangle)
```
- **Adding the Triangle to the Plot**: Adds the triangle to the Matplotlib axes (`ax`) using the [`add_patch` method](https://www.geeksforgeeks.org/matplotlib-axes-axes-add_patch-in-python/). This renders the triangle on the plot.

### draw_all_turtles function

`draw_all_turtles` takes multiple Turtle objects (and optionally a title) as arguments. It creates a Matplotlib plot showing the paths traced by each turtle and their current positions represented by symbols.

#### Computational Thinking

```python
    title = "Turtle Drawing"
    turtles_start_index = 0
```
- **Default Title Setup**: These lines defines the default title for the plot as `"Turtle Drawing"` and set `turtles_start_index` to 0. `turtles_start_index` is used to determine where in `args` the Turtle objects start.

```python
    if args and isinstance(args[0], str):
        title = args[0]
        turtles_start_index = 1
```
- **Title Argument Check**: checks if at least one argument was provided and if the first argument is a string. If so, it assumes the first argument (string) to be a custom title for the plot and updates the `title` variable. Also, it sets `turtles_start_index` to 1, indicating that Turtle objects start from the second argument in `args`.

- **Getting Current Axes**: A Matplotlib's `figure()` is initialised and [`gca()` (Get Current Axes)](https://www.geeksforgeeks.org/matplotlib-pyplot-gca-in-python/) is called to fetch the current axes, which will be used for plotting the turtle paths and symbols.


- **Iterating Over Turtle Objects**: the loop `for turtle in args[turtles_start_index:]:` iterates over each Turtle object passed in `args`, starting from `turtles_start_index`.

- **Retrieving Drawing Data**: `set_of_lines = turtle.get_drawing_data()` calls `get_drawing_data()` on each turtle to get a list of lines (paths) that the turtle has drawn.

- **Iterating Over Lines**: `for line in set_of_lines:` loop iterates over each line in `set_of_lines`. It unpacks each line's data into `start`, `end`, `color`, and `thickness`.

- **Plotting Lines**: `plt.plot` uses [Matplotlib's `plot()`](https://www.w3schools.com/python/matplotlib_plotting.asp) function to draw each line on the axes. It plots a line from `start` to `end` coordinates with the specified `color` and `linewidth`.

- **Drawing Turtle Symbols**: `draw_symbol(turtle, ax)` calls `draw_symbol` for each turtle, passing the current turtle and the axes `ax`. This draws the turtle's symbol on the plot at its current position.

- **Setting Plot Limits**: `plt.xlim` and `plt.ylim` set the limits for the x-axis and y-axis of the plot, respectively, using the `SCREEN_LIMIT` values from the configuration (`config.py`).

- **Adjusting Aspect Ratio**: `plt.gca().set_aspect()` ensures that the aspect ratio of the plot is equal, meaning one unit in x is of equal length to one unit in y, providing a uniform scale.

- **Displaying the Plot**: Finally, [`plt.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html) is called to display the plot with all the turtles' paths and symbols.