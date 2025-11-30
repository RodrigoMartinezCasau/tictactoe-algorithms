# Data Structures Used

This project combines several fundamental data structures studied in the course.

---

## 1. Multidimensional Arrays (Board Representation)

The board is represented as a list of lists in Python:

- The outer list stores rows.
- Each inner list stores the symbols in that row.
- A cell is accessed as `grid[row][col]`.

Properties:

- N×N structure where N can be chosen by the user (between 3 and 7 in Player vs Player mode).
- Easy to iterate over rows, columns and diagonals.
- Direct mapping to the concept of multidimensional arrays.

---

## 2. Classes and Encapsulation

The implementation uses three main classes:

### Board

Responsibilities:

- Store the N×N grid.
- Place moves at a given row and column.
- Check for a winner (rows, columns, diagonals).
- Detect whether the board is full.

This class encapsulates all operations that modify or inspect the state of the board.

### Game

Responsibilities:

- Manage the flow of a match.
- Configure the mode:
  - Player vs AI (fixed 3×3 board).
  - Player vs Player (board size 3–7).
- Ask the user for moves and validate input.
- Connect the `Board` and `AI` classes.

The `Game` class implements the high-level logic of the program but delegates the real work to `Board` and `AI`.

### AI

Responsibilities:

- Run the minimax algorithm to choose the best move on a 3×3 board.
- Evaluate terminal positions (win, loss, draw).
- Optionally cache positions in a hash table (memoization).

This clearly separates human logic (user input) from algorithmic decision making.

---

## 3. Hash Tables (Dictionaries) – Optional Memoization

To speed up minimax, a hash table can be used.  
In Python this is implemented as a dictionary:

- Keys are string encodings of the board plus the active player.
- Values are the minimax scores previously computed.

Advantages:

- Avoids recomputing the same position many times.
- Demonstrates the use of hash tables for caching results.

---

## 4. Call Stack and Recursion

The minimax algorithm is implemented recursively.  
Each recursive call stores on the call stack:

- The current board configuration.
- The current player.
- The depth in the game tree.

When a terminal state is reached, the function returns a score and the call stack is unwound, propagating the best scores upwards.

This connects the project to:

- Recursion
- The role of the call stack
- Depth-first search on trees

---

## 5. Simple Sequential Search

Winner detection and free-cell detection rely on sequential scans:

- Checking each row or column cell by cell.
- Checking all board cells to know if the game is a draw.

These operations are examples of linear scans over arrays with O(N) or O(N²) time complexity.
