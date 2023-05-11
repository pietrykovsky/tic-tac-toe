from typing import Tuple

from board import Board
from ai import MinimaxAI
from const import PLAYER_1, PLAYER_2, DRAW, PLAYER_1_WON, PLAYER_2_WON


class TicTacToe:
    def __init__(self, player: str, size: int, win_sequence: int, difficulty: int):
        self.board = Board(size, win_sequence)
        self.player = player
        self.ai = MinimaxAI(
            self.board, PLAYER_1 if player == PLAYER_2 else PLAYER_2, difficulty
        )

    def print(self):
        for row in self.board.grid:
            line = "| "
            for field in row:
                line += field + " | "
            line += "\n"
            print(line)

    def main_loop(self):
        while True:
            state = self.board.state()
            print("\n")
            self.print()
            if state == DRAW:
                print("DRAW")
                break
            if state == PLAYER_1_WON:
                print(f"{PLAYER_1} wins!")
                break
            if state == PLAYER_2_WON:
                print(f"{PLAYER_2} wins!")
                break
            if self.board.turn == self.player:
                while True:
                    row = int(input("row: "))
                    col = int(input("col: "))
                    if self.board.move(row, col):
                        break
            else:
                move = self.ai.get_move()
                self.board.move(*move)


TicTacToe("X", 5, 3, 8).main_loop()
