from copy import deepcopy

from board import Board
from const import PLAYER_1, PLAYER_2, NOT_FINISHED


class MinimaxAI:
    def __init__(self, board: Board, player: str, depth: int):
        self.board = board
        self.player = player
        self.depth = depth
        self.opponent = PLAYER_1 if player == PLAYER_2 else PLAYER_2

    def evaluate_state(self, board: Board, depth: int) -> float:
        if board.check_win(self.player):
            return 100 + depth
        if board.check_win(self.opponent):
            return -100 - depth
        possible_lines = board.get_possible_lines()
        potential_wins_1 = sum(self.player not in line for line in possible_lines)
        potential_wins_2 = sum(self.opponent not in line for line in possible_lines)
        return potential_wins_1 - potential_wins_2

    def minimax(
        self, board: Board, depth: int, alpha: float, beta: float
    ) -> tuple[float, tuple[int, int]]:
        if board.state() != NOT_FINISHED or depth == 0:
            return self.evaluate_state(board, depth), None
        best_move = None
        best_value = float("-inf") if board.turn == self.player else float("inf")

        for move in board.get_legal_moves():
            board_n = deepcopy(board)
            board_n.move(*move)
            eval_n, _ = self.minimax(board_n, depth - 1, alpha, beta)

            if board.turn == self.player:
                if eval_n > best_value:
                    best_value = eval_n
                    best_move = move
                alpha = max(alpha, eval_n)
            else:
                if eval_n < best_value:
                    best_value = eval_n
                    best_move = move
                beta = min(beta, eval_n)

            if alpha >= beta:
                break

        return best_value, best_move

    def get_move(self):
        if len(self.board.get_legal_moves()) == self.board.size**2:
            return self.board.size // 2, self.board.size // 2
        _, move = self.minimax(self.board, self.depth, float("-inf"), float("inf"))
        return move
