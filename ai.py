from copy import deepcopy
from collections import Counter

from board import Board
from const import PLAYER_1, PLAYER_2, NOT_FINISHED


class MinimaxAI:
    def __init__(self, board: Board, player: str, depth: int):
        self.board = board
        self.player = player
        self.depth = depth
        self.opponent = PLAYER_1 if player == PLAYER_2 else PLAYER_2

    def evaluate_state(self, board: Board) -> float:
        if board.check_win(self.player):
            return float("100")
        if board.check_win(self.opponent):
            return float("-100")
        possible_lines = board.get_possible_lines()
        potential_wins_1 = sum(PLAYER_2 not in line for line in possible_lines)
        potential_wins_2 = sum(PLAYER_1 not in line for line in possible_lines)
        return potential_wins_1 - potential_wins_2

    def minimax(
        self, board: Board, depth: int, alpha: float, beta: float
    ) -> tuple[float, tuple[int, int]]:
        moves = board.get_legal_moves()
        current_eval = self.evaluate_state(
            board
        )  # evalutation of the current state of the board
        if board.state() != NOT_FINISHED or depth == 0:
            return current_eval, None
        best_value = float("-inf") if board.turn == self.player else float("inf")
        best_move = None
        for move in moves:
            board_n = deepcopy(board)
            board_n.move(*move)
            best_value_n, _ = self.minimax(board_n, depth - 1, alpha, beta)
            if board.turn == self.player:
                if best_value_n > best_value:
                    best_value = best_value_n
                    best_move = move
                alpha = max(alpha, best_value_n)
            else:
                if best_value_n < best_value:
                    best_value = best_value_n
                    best_move = move
                beta = min(beta, best_value_n)
            del board_n
            if alpha >= beta:
                break
        return best_value, best_move

    def get_move(self):
        if len(self.board.get_legal_moves()) == self.board.size**2:
            return self.board.size // 2, self.board.size // 2
        e, move = self.minimax(self.board, self.depth, float("-inf"), float("inf"))
        print(e)
        return move
