# 🧠 Ultimate Tic Tac Toe – Human vs AI

Ultimate Tic Tac Toe is a strategic twist on the classic game of Tic Tac Toe. In this implementation, you play against a competitive AI that uses **Minimax with Alpha-Beta Pruning** for decision-making, ensuring intelligent and fast responses.

---

## 🎮 Game Concept

In **Ultimate Tic Tac Toe**, the game board is made up of 9 smaller Tic Tac Toe boards arranged in a 3x3 grid – forming a large “meta-board”.

### Rules Overview:

- Each move you make within a **small board** also determines which board your opponent will be sent to next.
- The position of your move (1 through 9) maps directly to one of the 9 small boards.
- For example, placing your symbol in the **top-left cell (position 1)** of any board will send your opponent to the **top-left board** next.
- If the target board is already completed (won or tied), the opponent can choose any unfinished board.

### Victory Conditions:

- Winning a **small board** secures that cell in the **global board**.
- To win the game, a player must capture **three small boards in a row** (horizontally, vertically, or diagonally) – just like classic Tic Tac Toe but on the global scale.

---

## 📐 Board Layout

Each of the 9 small boards and the global board follow a standard Tic Tac Toe layout:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
---------

- The **meta-board** is also structured using this layout.
- Once a small board is won, it will be marked with a stylized `"X"` or `"O"` across its cells.
- If it ends in a tie, all cells will be filled with `"T"`.

---

## 🤖 AI Features

- Implements **Minimax** with **Alpha-Beta Pruning** for deep, strategic evaluation of the game tree.
- Intelligent local and global decision-making: the AI evaluates both the current board and the overall state.
- Automatically reroutes its strategy if forced into completed boards.
- Includes time-limited recursion to ensure real-time responsiveness.

---

## 🧩 Code Structure

| File         | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `main.py`    | Entry point of the application. Launches the game loop.                     |
| `game.py`    | Manages game flow, user prompts, and turn logic for human vs AI gameplay.   |
| `board.py`   | Models the entire 9x9 Ultimate Tic Tac Toe board, with win/tie logic.        |
| `ai.py`      | Contains the AI logic using Minimax and Alpha-Beta pruning with time limits. |

---

## ✅ How to Run

### Requirements

- Python 3.x
- No external libraries required

### Run the Game

```bash
python main.py
