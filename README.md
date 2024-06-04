# Sudoku Solver

This repository contains a Python implementation of a Sudoku solver for 9x9 Sudoku puzzles. The algorithm takes a partially filled Sudoku grid from an input file and fills in the missing numbers while adhering to the rules of Sudoku. The solved puzzle is then output to a new file.

## Features

- Solves standard 9x9 Sudoku puzzles.
- Simple and straightforward implementation.
- No external dependencies required.
- Reads puzzle input from a file and writes the solution to a new file.

## Example

### Input (in `sudo_example.txt`)

```
8, 0, 0, 0, 0, 0, 0, 0, 0
0, 0, 3, 6, 0, 0, 0, 0, 0
0, 7, 0, 0, 9, 0, 2, 0, 0
0, 5, 0, 0, 0, 7, 0, 0, 0
0, 0, 0, 0, 4, 5, 7, 0, 0
0, 0, 0, 1, 0, 0, 0, 3, 0
0, 0, 1, 0, 0, 0, 0, 6, 8
0, 0, 8, 5, 0, 0, 0, 1, 0
0, 9, 0, 0, 0, 0, 4, 0, 0
```


### Output (in `result.txt`)

```
8, 1, 2, 7, 5, 3, 6, 4, 9
9, 4, 3, 6, 8, 2, 1, 7, 5
6, 7, 5, 4, 9, 1, 2, 8, 3
1, 5, 4, 2, 3, 7, 8, 9, 6
3, 6, 9, 8, 4, 5, 7, 2, 1
2, 8, 7, 1, 6, 9, 5, 3, 4
5, 2, 1, 9, 7, 4, 3, 6, 8
4, 3, 8, 5, 2, 6, 9, 1, 7
7, 9, 6, 3, 1, 8, 4, 5, 2
```


## Getting Started

### Prerequisites

- Python 3.x

### Running the Solver

1. Clone the repository:
    ```bash
    git clone https://github.com/mitko-stoyanov/Sudoku
    cd sudoku-solver
    ```

2. Ensure you have Python installed on your system.

3. Create a file named `sudoku_example.txt` with your Sudoku puzzle input in the same directory as the script.

4. Run the script:
    ```bash
    python sudoku_solver.py
    ```

5. The solved Sudoku puzzle will be written to `result.txt`.

## How It Works

The algorithm uses a backtracking approach to solve the Sudoku puzzle. It tries to place numbers in empty cells one by one, checking if the number placement is valid according to Sudoku rules. If a placement is valid, it recursively attempts to solve the rest of the puzzle with this new placement. If it encounters a conflict, it backtracks and tries the next number.
