# 🎮 TicTacToe — Algorithms & Data Structures Project

This project implements a complete **Tic Tac Toe** game in Python, developed for the **Algorithms & Data Structures** course.  
The goal is to demonstrate proper use of data structures, clean modular design, testing, and algorithmic reasoning.

---

## 📁 Project Structure

tictactoe-algorithms/
│
├── docs/
│ ├── algorithms_exp.md # Explanation of the algorithms used
│ ├── data_structure.md # Data structures chosen and why
│ └── presentation_notes.md # Notes for the oral presentation
│
├── src/
│ ├── board.py # Board class: grid, moves, validation
│ ├── player.py # Player class: symbol & identification
│ ├── game.py # Main TicTacToe game logic
│ └── main.py # Entry point (terminal gameplay)
│
├── tests/
│ └── test_game.py # Unit tests using unittest
│
├── .gitignore
└── README.md

---

## 🧠 Concepts Demonstrated

### ✔️ 1. Modular Programming
The project is separated into clear components:
- **Board** → manages the 3×3 matrix and game rules  
- **Player** → abstraction of each participant  
- **TicTacToe (Game)** → core algorithm and state machine  
- **main.py** → user interaction and game loop  

### ✔️ 2. Data Structures
Core data structures used:

- **2D lists (matrices)** — board representation  
- **Lists** — winner detection  
- **Tuples** — coordinate representation  
- **Strings** — symbols (`"X"`, `"O"`) and state messages  

These choices balance simplicity and performance for a small board-based game.

### ✔️ 3. Algorithms
Key algorithms implemented:

- **Turn alternation algorithm**  
- **Move validation algorithm**  
- **Winner detection algorithm** checking:
  - Rows  
  - Columns  
  - Main diagonal  
  - Anti-diagonal  
- **Draw detection algorithm**  
- **State evaluation algorithm** (win / draw / ongoing)

All algorithms run in **O(1)** time because the board is fixed (3×3).

### ✔️ 4. Unit Testing (unittest)
Test cases include:

- Empty board state  
- Horizontal win  
- Vertical win  
- Diagonal win  
- Turn switching  
- Draw scenario  

---

## ▶️ How to Run the Game

1. Clone the repository:

git clone https://github.com/RodrigoMartinezCasau/tictactoe-algorithms.git

2. Navigate to the source folder:

cd ~/tictactoe-algorithms/src

3. Run the game:

python3 main.py

---

## 🧪 Run Unit Tests

From the project root:

python3 -m unittest tests/test_game.py

---

## 🎤 Presentation Guide (10 minutes)

A recommended structure for your oral presentation:

### **1. Introduction (30 seconds)**
- What the project is  
- What it demonstrates  

### **2. Architecture Overview (2 minutes)**
- Folder structure  
- How Board, Game, and Player interact  

### **3. Data Structures (2 minutes)**
- Why a 2D list  
- Why tuples  
- Simplicity and low overhead  

### **4. Algorithms (3 minutes)**
- How winner detection works  
- How the game loop operates  
- Edge cases handled  

### **5. Unit Testing (1 minute)**
- Why tests are important  
- Examples of test cases  

### **6. Conclusion (30 seconds)**
- Clean modular design  
- Easy to extend  
- Demonstrates course concepts effectively  

---

## 🌟 Future Improvements (Optional)

- AI opponent using **Minimax**  
- **Undo/Redo** using stacks  
- Graphical UI using **game2board**  
- Online multiplayer version  

---

## 👨‍💻 Authors

Developed by the **IE University TicTacToe Team**:
- Rodrigo Martínez Casau  
- David Andrei Dumitrescu  
- Khadeja Nehad  
- Ralph Patrick François  

---

## 📄 License

This project is provided for educational purposes as part of the *Algorithms & Data Structures* course.