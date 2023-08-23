# Tic Tac Toe Game With AI

A Python-based Tic Tac Toe game with AI capabilities. Play against a friend or challenge the AI opponent!

<div align="center">
  <img src="./images/screenshot.png" alt="Project Screenshot" width="400">
</div>

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)

## Features

- AI comes in two modes, level 0 and 1.
  - In Level 0, AI makes random moves.
  - In Level 1, the AI is unbeatable (will either win or draw).
- Visual indication of a line when three X's or O's align.
- Easy placement of X's and O's by clicking on the squares.
- Implementation of the minimax algorithm with alpha-beta pruning for improved efficiency.

## Usage

- Run the code to start the game (AI level is set to 1 by default).
- To switch between AI levels:
  - Press '0' on the keyboard for Level 0 AI.
  - Press '1' on the keyboard for Level 1 AI (unbeatable).
- To switch to two-player mode (no AI):
  - Press 'g' on the keyboard.
- To reset the game and clear all values:
  - Press 'r' on the keyboard.

## Installation

To get started and play the AI Tic Tac Toe game on your local machine, follow these steps:

1. **Clone the Repository:**
   Open your terminal and use the following command to clone this repository to your local machine:
   ```bash
   git clone https://github.com/ArmanGrewal03/ai-tictack.git
2.**Navigate to the Game Directory:**
  Move into the game directory that you just cloned using the following command:
   cd ai-tictack
3.**Install Dependencies:**
  Before you run the game, make sure you have the necessary dependencies installed. If you haven't already, use      the following commands to install pygame and numpy:
   pip install pygame
   pip install numpy
4.**Run the Game:**
  After installing the dependencies, you're ready to run the game:
  python tictactoe.py

  


