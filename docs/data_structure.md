# Data Structures Used

## 1. 2D Matrix (List of Lists)

The game board is represented using a 3×3 matrix:

- Each row is a list.
- The board is a list containing three row lists.
- This structure allows intuitive access with `board[row][col]`.

Advantages:
- Fast indexing.
- Easy to visualize.
- Matches the layout of the game.

---

## 2. Player Class

Each player is represented as an object containing:
- A name.
- A symbol (“X” or “O”).

This abstraction improves readability and modularity.

---

## 3. Board Class

The Board class stores:
- The 3×3 grid.
- Methods to place marks.
- Methods to reset the grid.
- A method to check if the board is full.

It acts as an Abstract Data Type managing the game state.

---

## 4. Game Class

The Game class connects components:
- Keeps track of the current player.
- Validates moves.
- Checks for end-state conditions.
- Manages turn switching.

Acts as the controller of the system.

---

## 5. Algorithms as Separate Functions

Winner-detection logic is stored in standalone functions inside `algorithms.py`.

Advantages:
- Cleaner code.
- Easier testing.
- Independent from the Game and Board logic.

---

## 6. Alternatives Considered

### A. Dictionary-Based Board
Rejected because a matrix better represents spatial layout.

### B. Single List of 9 Cells
Possible, but less readable than a 2D matrix.

### C. Graph Representation
Too complex for a 3×3 board.

### D. Sets for Win Conditions
Possible, but less clear for diagonals.

---

## Conclusion

The chosen structures (matrix + classes + modular functions) create:
- Clear architecture.
- Efficient algorithms.
- Easy maintainability.
- Perfect educational value for an Algorithms & Data Structures project.
