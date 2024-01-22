# Turtle Graphics Project

## Project Description

The Turtle Graphics Project is an implementation of a turtle graphics system, a key feature in many learning environments for programming. This system allows users to create drawings and patterns using simple commands that control a "turtle" on a canvas. This project is structured to offer both example scripts and a framework for users to create their own turtle-based drawings.

## Requirements

- Python 3.x
- Matplotlib library (for drawing capabilities)

To install the required library, run:
```bash
pip install matplotlib
```

## Features of the Turtle Graphics Project

1. **Turtle Movement**: Includes forward and backward movements, allowing the turtle to navigate the canvas.
2. **Directional Control**: The turtle can turn left or right, adjusting its heading angle.
3. **Pen Control**: Offers the ability to lift or drop the pen, enabling or disabling drawing as the turtle moves.
4. **Drawing Circles**: A dedicated method to draw circular arcs of specified radius and extent.
5. **Customisable Appearance**: Users can change the turtle's line colour and thickness and the colour of the turtle's symbol representation on the canvas.
6. **Position Tracking**: The turtle's current position can be retrieved, which is useful for complex drawings or tracking movements.
7. **Drawing Data Storage**: The turtle records its drawn paths for potential rendering or analysis.
8. **Reset Functionality**: Allows resetting the turtle to its initial state, clearing its drawing history.
9. **Direct Navigation**: Provides a `goto` method for direct movement to specified coordinates, bypassing incremental steps.
10. **Screen Boundary Enforcement**: The turtle's movements are constrained within defined screen limits, ensuring it stays within the visible area.

## Implementing Your Own Turtle Drawing

To create your turtle drawing:
1. Edit the `my_turtle_template.py` file in the root directory. This file is set up so you can start coding with the Turtle class immediately.
2. Alternatively, you can create new Python files in the root directory. Make sure to import the Turtle class from the `turtle_graphics` package.
3. **The exercise of this interview is available**. Open your `cmd` prompt, navigate to the project's root directory using `cd /path/to/root_directory`, and from the root directory, type `python interview_exercise.py` to run it.

## Running Examples

The `examples/` directory contains pre-written example scripts demonstrating different capabilities of the Turtle class.

To run an example, navigate to the project's root directory and execute:
```bash
python -m examples.example_1
```
Replace `example_1` with the name of the example you want to run.

## Running Tests

The `tests/` folder contains unit tests for both the Turtle class (`test_turtle.py`) and the drawing functionality (`test_drawing.py`).

To run the tests, use the following command from the project's root directory:
```bash
python -m unittest tests.test_turtle
```
Replace `test_turtle` with `test_drawing` to run the tests for the drawing functionality.

### About the Tests

- `test_turtle.py`: Contains tests for various methods of the Turtle class, ensuring correct movement, pen control, and other functionalities.
- `test_drawing.py`: Tests the drawing output of the Turtle class, validating the correct rendering of lines and shapes.

## Next Steps: suggested modifications for students

1. User Inputs for Turtle Movements: consider enhancing the system by allowing user inputs to define turtle movements. For example, using command-line inputs or GUI-based controls.

2. Ensure that SOLID principles are followed for OOP implementations. Currently, this project follows only the Single-Responsability Principle (SRP). Adding other applicable principles, such as the Open-Closed Principle (OCP), is recommended. OCP will also bring OOP abstraction to the project.

3. Write a comprehensive documentation covering setup, usage, examples, and detailed explanation of computational thinking.

4. Optimisation Techniques: as the complexity of the drawings increases, consider implementing optimisation techniques:
- Batch processing of drawing commands.
- Efficient data structures for storing line data.
- Using GPU-based libraries for rendering.

5. Alternative Graphics Methods: while currently using Matplotlib for graphics, exploring other libraries like Pygame, OpenCV, or even web-based technologies like HTML5 Canvas (for a web version) could offer different capabilities and performance characteristics.

## Good Practices followed for this project to be kept for the next steps

1. **Modular Design**: The project is structured into separate modules, enhancing readability and maintainability.

2. **Clean Code**: The code is written clearly and concisely, making it easy to understand and modify.

3. **Documentation**: Each class and method is well-documented with docstrings, comments, and annotations, providing clear descriptions and usage instructions. Readme files are also provided with brief explanations. *A full written documentation is under development*.

4. **Error Handling**: Robust error handling is implemented to manage incorrect inputs and edge cases effectively.

5. **Code Consistency**: Consistent naming conventions and coding styles are maintained throughout the project, ensuring uniformity.

6. **Encapsulation**: The project uses encapsulation to hide complex implementation details, providing a simple interface for users.

7. **Separation of Concerns**: Each class and method has a single, well-defined purpose, adhering to the Single Responsibility Principle (SRP).

8. **Testing**: Comprehensive test cases cover various functionalities, ensuring the reliability and stability of the code.

9. **Scalability and Flexibility**: The design allows for adding new features and functionalities easily.

10. **Adherence to Standards**: The project follows standard programming practices and guidelines, such as PEP8 for Python.

11. **User-Centric Design**: Focus on user experience and ease of use with a straightforward naming convention, making the project accessible to a wider audience.

These practices enhance code quality by increasing readability, maintainability, and usability.
