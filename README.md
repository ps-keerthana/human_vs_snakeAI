# Human vs Snake AI – Performance Comparison 🎮🤖

This repository presents a fun and insightful **Python project** built using `pygame`, where a **manual player (human)** competes against an **AI-controlled snake** in the classic Snake Game.

The twist?  
➡️ The AI plays the exact same game using the **same food positions** as the manual player.  
This allows us to compare their **efficiency, accuracy**, and gameplay style!

---

## 🎬 Demo GIF

> 🕹️ Manual Player → 🤖 AI Snake → 📊 Final Stats

![Snake Game Demo](assets/demo.gif)

---

## 🔍 Project Highlights

- 🎮 **Manual Gameplay**: Control the snake using arrow keys
- 🤖 **AI Gameplay**: AI uses pathfinding to collect the same food sequence
- 📊 **Live Stats Panel**: See mode, moves, food eaten, and FPS live
- 🧠 **Smart AI Logic**: BFS-style pathfinding to avoid collisions and walls
- 🏁 **Final Comparison**: Shows accuracy, move efficiency, and food collection side-by-side

---

## 🧠 Core Concepts Implemented

- Game development using `pygame`
- Real-time stats panel
- AI decision-making logic
- Performance metrics logging
- Manual vs AI comparison framework

---

## Performance Metrics Explained

### 🧠 Efficiency:
> **Efficiency (%) = (AI Moves / Manual Moves) × 100**

Shows how optimized the AI path is compared to the human.

### 🎯 Accuracy:
> **Accuracy (%) = Efficiency (%)**

Manual player's accuracy is defined by how close their path length is to the AI’s.

---

## 🛠️ Setup Instructions

Follow these steps to set up and run the project locally:

```bash
# 📌 1. Check your Python version (should be 3.7+)
python --version

# 📌 2. Create a virtual environment (optional but recommended)
python -m venv myenv

# 📌 3. Activate the environment

# On Windows:
myenv\Scripts\activate

# On macOS/Linux:
source myenv/bin/activate

# 📌 4. Install dependencies
pip install pygame

# 📌 5. Run the game
python snake_game.py
