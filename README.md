# tic-tac-toe
Simple Python tictactoe game with alpha beta pruning minimax AI implemented with pygame.

## Features
* simple GUI in pygame
* minimax based AI with adjusted difficulty
* choice of board size and winning sequence length

## Requirements
* python 3.10

## Installation
Firstly, clone the repository from the github to your local folder with the following command:
```bash
git clone https://github.com/pietrykovsky/tic-tac-toe.git
```

Next, create virtual environment and install dependencies:
```bash
python -m venv venv

source venv/bin/activate #linux
or
.\venv\Scripts\activate #windows

pip install -r requirements.txt
```

## Usage
To choose the board size and player modify following parameters in `config.py`:
```python
# START AS A PLAYER 1 (X) OR PLAYER 2 (O)
PLAYER = PLAYER_2

# SIZE OF THE BOARD
BOARD_SIZE = 3

# LENGTH OF THE WINNING SEQUENCE
WIN_SEQUENCE = 3

# DEPTH OF THE MINIMAX ALGORITHM
AI_DIFFICULTY = 8
```
Keep in mind that higher AI difficulty may be very slow combined with big board size and small winning sequence length. I recommend to use `AI_DIFFICULTY = 8` for `BOARD_SIZE = 3` and `WIN_SEQUENCE = 3`, and `AI_DIFFICULTY = 4` for bigger sizes.

Now you can start the game by typing following command:
```bash
python tictactoe.py
or
python3 tictactoe.py
or
py tictactoe.py
```
