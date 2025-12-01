# Algorithms Explanation

This project implements several key algorithms from the Algorithms & Data Structures course.

## 1. Minimax (AI Player)

Minimax is a recursive decision-making algorithm used in game theory.  
In this project it is used for the AI on a 3×3 board.

Main ideas:

- The AI assumes that the opponent always plays optimally.
- The game tree is explored with depth-first search (DFS).
- Each terminal position is evaluated as:
  - +1 if the AI wins
  - −1 if the AI loses
  - 0 for a draw
- The AI chooses the move that maximizes its final score.

This directly connects to:

- Recursion
- Trees
- DFS (Depth First Search)
- Algorithm analysis (exponential time on large boards)

### Complexity

On a 3×3 board the branching factor is at most 9 moves at the first level and then decreases.  
The full game tree has around 255k states, which is still manageable.

For bigger boards the number of possible positions grows exponentially, so running full minimax becomes impractical. That is why the AI mode is restricted to 3×3.

---

## 2. Winner Detection

The board is an N×N grid stored as a list of lists.  
The algorithm to detect a winner checks:

- All rows
- All columns
- The main diagonal
- The anti-diagonal

For each line, the algorithm verifies that:

- All cells are equal.
- None of the cells is the empty symbol.

If this happens, that symbol is the winner.  
If all cells on the board are filled and there is no winning line, the result is a draw.

Time complexity:

- Checking a single line: O(N)
- Checking all lines on the board: O(N²)


