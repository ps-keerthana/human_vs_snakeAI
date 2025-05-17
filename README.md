# Human vs Snake AI – Performance Comparison 🎮🤖

This repository contains a Python project that compares how a **manual (human)** player and an **AI** perform in the classic Snake Game using `pygame`. The AI is tested using the **same food positions** as the human, and their performance is compared in terms of total moves and efficiency.

---
## Project Overview

- Manual gameplay: You control the snake with arrow keys.
- AI gameplay: The AI mimics the food sequence collected by the manual player and uses pathfinding to reach food.
- Final output: Shows both players’ food count, number of moves, efficiency, and accuracy comparison.

---

## Core Concepts Implemented

1. **Game Development using `pygame`**
2. **AI Pathfinding**
3. **Data Logging & Analysis**
4. **Performance Metrics**:
   - Number of moves taken
   - Food collected
   - Efficiency comparison
   - Accuracy of manual player based on AI performance
---
## 📦 Getting Started

To set up the environment and run this project, follow the steps below:

```bash
# Check Python and pip versions
python --version
pip --version

# Create a virtual environment
python -m venv myenv

# Activate the virtual environment

# For Windows:
myenv\Scripts\activate
# For macOS/Linux:
source myenv/bin/activate

# Install pygame
pip install pygame

# Run the main game file
python snake_game.py


