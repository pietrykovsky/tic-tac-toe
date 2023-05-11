from const import (
    EMPTY,
    PLAYER_1,
    PLAYER_2,
    PLAYER_1_WON,
    PLAYER_2_WON,
    DRAW,
    NOT_FINISHED,
)


class Board:
    def __init__(self, size: int = 3, win_sequence: int = 3):
        self.size: int = size
        self.win_sequence: int = win_sequence
        self.turn = PLAYER_1
        self.grid: list = [[EMPTY for _ in range(self.size)] for _ in range(self.size)]

    def get_legal_moves(self) -> list[(int, int)]:
        moves = []
        for y, row in enumerate(self.grid):
            for x, field in enumerate(row):
                if field == EMPTY:
                    moves.append((y, x))
        return moves

    def move(self, row: int, col: int) -> bool:
        if self.is_move_possible(row, col):
            self.grid[row][col] = self.turn
            self.turn = PLAYER_1 if self.turn == PLAYER_2 else PLAYER_2
            return True
        return False

    def is_move_possible(self, row: int, col: int):
        if row < self.size and col < self.size:
            if self.grid[row][col] == EMPTY:
                return True
        return False

    def state(self) -> int:
        """
        Check if the game is over.

        :return: -1 if the game is not over, 0 if it is a tie, 1 if the player 1 won, 2 if the player 2 won
        :rtype: int
        """
        if self.check_win(PLAYER_1):
            return PLAYER_1_WON
        if self.check_win(PLAYER_2):
            return PLAYER_2_WON
        if self.is_full():
            return DRAW
        return NOT_FINISHED

    def is_full(self):
        for row in self.grid:
            for field in row:
                if field == EMPTY:
                    return False
        return True

    def get_possible_lines(self) -> list:
        lines = []

        # Check rows
        for row in range(self.size):
            for col in range(self.size - self.win_sequence + 1):
                line = [self.grid[row][col + i] for i in range(self.win_sequence)]
                lines.append(line)

        # Check columns
        for col in range(self.size):
            for row in range(self.size - self.win_sequence + 1):
                line = [self.grid[row + i][col] for i in range(self.win_sequence)]
                lines.append(line)

        # Check main diagonals
        for row in range(self.size - self.win_sequence + 1):
            for col in range(self.size - self.win_sequence + 1):
                line = [self.grid[row + i][col + i] for i in range(self.win_sequence)]
                lines.append(line)

        # Check anti-diagonals
        for row in range(self.size - self.win_sequence + 1):
            for col in range(self.win_sequence - 1, self.size):
                line = [self.grid[row + i][col - i] for i in range(self.win_sequence)]
                lines.append(line)

        return lines

    def check_win(self, player):
        # Check rows
        for row in range(self.size):
            for col in range(self.size - self.win_sequence + 1):
                if all(
                    self.grid[row][col + i] == player for i in range(self.win_sequence)
                ):
                    return True

        # Check columns
        for col in range(self.size):
            for row in range(self.size - self.win_sequence + 1):
                if all(
                    self.grid[row + i][col] == player for i in range(self.win_sequence)
                ):
                    return True

        # Check main diagonals
        for row in range(self.size - self.win_sequence + 1):
            for col in range(self.size - self.win_sequence + 1):
                if all(
                    self.grid[row + i][col + i] == player
                    for i in range(self.win_sequence)
                ):
                    return True

        # Check anti-diagonals
        for row in range(self.size - self.win_sequence + 1):
            for col in range(self.win_sequence - 1, self.size):
                if all(
                    self.grid[row + i][col - i] == player
                    for i in range(self.win_sequence)
                ):
                    return True

        return False
