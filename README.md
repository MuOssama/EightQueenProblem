# 8 Queens Problem

This Python program uses Pygame to visualize the solution to the 8 Queens Problem using a genetic algorithm.

## Setup

1. **Initialize Pygame**: The program initializes Pygame to create a graphical window.

2. **Constants**: Defines constants such as the window dimensions, cell size, and colors.

3. **Load Queen Image**: Loads and scales the queen image to be used on the chessboard.

## Functions

### `draw_board(screen)`

- Draws the chessboard on the screen.

### `draw_queens(screen, queens)`

- Draws the queens on the board based on their positions.

### `solve_queens(initial_board, population_size, mutation_rate, max_generations)`

- Solves the 8 Queens Problem using a genetic algorithm.
- Defines fitness, crossover, and mutation functions.
- Initializes and evolves the population to find the solution.

### `main()`

- Main function to run the game loop.
- Handles user input to place queens and start the algorithm.
- Displays the chessboard and queens on the screen.
- Saves the solution as an image when found.

## Running the Program

1. Run the program.
2. Click on the chessboard to place queens.
3. Press SPACE to start the genetic algorithm.
4. Once a solution is found, the queens will be placed on the board, and the solution will be printed.

## How to Use

1. Ensure you have Python and Pygame installed.
2. Place the `queen.png` image in the same directory as the script.
3. Run the script and follow the on-screen instructions.

## Dependencies

- Python 3.x
- Pygame
