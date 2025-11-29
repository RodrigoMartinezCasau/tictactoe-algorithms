# Algorithm Explanations

## 1. Row Winner Check

A row is a winning row if all its three cells contain the same symbol and are not empty.

Complexity: O(1)

---

## 2. Column Winner Check

A column is a winning column if the three cells in that column match and are not empty.

Complexity: O(1)

---

## 3. Diagonal Winner Check

Two diagonals are checked:

- Main diagonal: (0,0), (1,1), (2,2)
- Secondary diagonal: (0,2), (1,1), (2,0)

A diagonal is a winning diagonal if all three positions match.

Complexity: O(1)

---

## 4. Board Full Check

Checks if the board has any empty spaces left.  
Since the board is always 3×3, the operation is constant.

Complexity: O(1)

---

## 5. Turn Switching

Turns alternate using a simple toggle between two Player instances.

Complexity: O(1)

---

## Summary

All core game algorithms run in **constant time O(1)** due to the fixed size of the grid (3×3).  
This guarantees optimal performance for the board game logic.
