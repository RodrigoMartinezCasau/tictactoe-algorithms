# Presentation Notes

These notes are intended as a guide for the oral presentation of the project.

---

## Slide 1 – Overview

- Our project is a TicTacToe game implemented in Python.
- It has two main modes:
  - Player vs AI (3×3 board, using minimax).
  - Player vs Player (board size between 3 and 7).
- The code is written using classes: `Board`, `Game` and `AI`.

Key sentence to say:
> The main idea was to take a very simple game and use it as a playground to connect many topics from the Algorithms & Data Structures course.

---

## Slide 2 – Key Algorithms

Bullet points to mention:

- Minimax algorithm for AI decision making.
- Winner detection in O(N²) by scanning rows, columns and diagonals.
- Depth-first search through the game tree using recursion.
- Optional memoization using a hash table to store evaluated positions.

Possible explanation:
> Minimax explores possible future moves, assuming both players play optimally, and chooses the move that maximizes the AI’s final outcome.

---

## Slide 3 – Data Structures

Points to highlight:

- The board is an N×N multidimensional array (list of lists).
- We use three classes:
  - `Board`: manages the grid and winner detection.
  - `Game`: controls turns, input and configuration.
  - `AI`: runs minimax and returns the best move.
- Recursion uses the call stack implicitly, which can be linked to the stacks topic.

---

## Slide 4 – Course Concepts Covered

List of course topics that appear in the project:

- Recursion (minimax).
- DFS and trees (game tree exploration).
- Multidimensional arrays (board).
- Hash tables (memoization).
- Sequential search (winner detection).
- Algorithm analysis (complexity of minimax and board scanning).

You can say:
> With one small game we managed to touch almost every topic from the second half of the course.

---

## Slide 5 – Why AI Only on 3×3

Key ideas:

- Minimax has exponential complexity with respect to the number of cells.
- The 3×3 board has around 255k possible game states.
- For 5×5 or 7×7 the number of states explodes and would be too slow.

Nice sentence:
> The AI looks smart, but in reality it is just brutally exploring the whole game tree; that is why we keep it on a 3×3 board.

---

## Slide 6 – Demo Plan

Suggested order:

1. Run the program and choose Player vs AI.
2. Show a couple of moves, highlighting that the AI never loses.
3. Restart in Player vs Player mode and choose a larger board (for example 5×5).
4. Briefly show that the logic still works for different sizes.

---

## Slide 7 – Conclusion

Points to close the presentation:

- The project combines theory (algorithms and data structures) with a concrete game.
- It demonstrates how recursion, trees, hash tables and arrays can be used together.
- Possible future improvements:
  - Better evaluation functions for non-terminal states.
  - A graphical user interface using a library like `game2board` or similar.

Final line:
> Overall, TicTacToe turned out to be a very good excuse to practice real algorithms instead of just solving abstract exercises.
