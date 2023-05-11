import pygame

from board import Board
from ai import MinimaxAI
from const import PLAYER_1, PLAYER_2, PLAYER_1_WON, PLAYER_2_WON, DRAW, NOT_FINISHED

# Initialize Pygame
pygame.init()

# Set screen dimensions and colors
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)

# Set players
HUMAN = PLAYER_1
AI = PLAYER_2

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the game board
board = Board(5, 5)
ai = MinimaxAI(board, AI, 8)


def draw_board():
    for row in range(1, board.size):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, HEIGHT // board.size * row),
            (WIDTH, HEIGHT // board.size * row),
            board.size,
        )
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (WIDTH // board.size * row, 0),
            (WIDTH // board.size * row, HEIGHT),
            board.size,
        )

    for row in range(board.size):
        for col in range(board.size):
            symbol = board.grid[row][col]
            if symbol == PLAYER_2:
                pygame.draw.circle(
                    screen,
                    BLACK,
                    (
                        col * WIDTH // board.size + WIDTH // (2 * board.size),
                        row * HEIGHT // board.size + HEIGHT // (2 * board.size),
                    ),
                    WIDTH // (2 * board.size) - 10,
                    board.size,
                )
            elif symbol == PLAYER_1:
                pygame.draw.line(
                    screen,
                    BLACK,
                    (
                        col * WIDTH // board.size
                        + WIDTH // (2 * board.size)
                        - WIDTH // (2 * board.size)
                        + 10,
                        row * HEIGHT // board.size
                        + HEIGHT // (2 * board.size)
                        - HEIGHT // (2 * board.size)
                        + 10,
                    ),
                    (
                        col * WIDTH // board.size
                        + WIDTH // (2 * board.size)
                        + WIDTH // (2 * board.size)
                        - 10,
                        row * HEIGHT // board.size
                        + HEIGHT // (2 * board.size)
                        + HEIGHT // (2 * board.size)
                        - 10,
                    ),
                    board.size,
                )
                pygame.draw.line(
                    screen,
                    BLACK,
                    (
                        col * WIDTH // board.size
                        + WIDTH // (2 * board.size)
                        + WIDTH // (2 * board.size)
                        - 10,
                        row * HEIGHT // board.size
                        + HEIGHT // (2 * board.size)
                        - HEIGHT // (2 * board.size)
                        + 10,
                    ),
                    (
                        col * WIDTH // board.size
                        + WIDTH // (2 * board.size)
                        - WIDTH // (2 * board.size)
                        + 10,
                        row * HEIGHT // board.size
                        + HEIGHT // (2 * board.size)
                        + HEIGHT // (2 * board.size)
                        - 10,
                    ),
                    board.size,
                )


# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and board.turn == HUMAN:
            x, y = pygame.mouse.get_pos()
            row, col = y // (HEIGHT // board.size), x // (WIDTH // board.size)
            if board.is_move_possible(row, col):
                board.move(row, col)

    if board.turn == AI:
        move = ai.get_move()
        if move is not None:
            board.move(*move)

    draw_board()
    pygame.display.flip()

    state = board.state()
    if state != NOT_FINISHED:
        print(
            "Player 1 won!"
            if state == PLAYER_1_WON
            else "Player 2 won!"
            if state == PLAYER_2_WON
            else "It's a draw!"
        )
        pygame.time.delay(board.size)
        running = False
        pygame.quit()
