import pygame

from board import Board
from ai import MinimaxAI
import const
import config as cfg


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.size = const.WIDTH, const.HEIGHT
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(const.GAME_TITLE)
        self.board = Board(cfg.BOARD_SIZE, cfg.WIN_SEQUENCE)
        self.ai = MinimaxAI(
            self.board,
            const.PLAYER_1 if cfg.PLAYER == const.PLAYER_2 else const.PLAYER_2,
            cfg.AI_DIFFICULTY,
        )

    def draw_text(self, text: str):
        w, h = self.size
        font = pygame.font.SysFont("Comic Sans MS", 50, True)
        text_surface = font.render(text, False, const.BLACK)
        self.screen.blit(text_surface, (w // 2 - 100, h // 2 - 30))

    def draw_board(self):
        self.screen.fill(const.WHITE)
        for row in range(1, self.board.size):
            pygame.draw.line(
                self.screen,
                const.LINE_COLOR,
                (0, const.HEIGHT // self.board.size * row),
                (const.WIDTH, const.HEIGHT // self.board.size * row),
                self.board.size,
            )
            pygame.draw.line(
                self.screen,
                const.LINE_COLOR,
                (const.WIDTH // self.board.size * row, 0),
                (const.WIDTH // self.board.size * row, const.HEIGHT),
                self.board.size,
            )

        for row in range(self.board.size):
            for col in range(self.board.size):
                symbol = self.board.grid[row][col]
                if symbol == const.PLAYER_2:
                    pygame.draw.circle(
                        self.screen,
                        const.RED,
                        (
                            col * const.WIDTH // self.board.size
                            + const.WIDTH // (2 * self.board.size),
                            row * const.HEIGHT // self.board.size
                            + const.HEIGHT // (2 * self.board.size),
                        ),
                        const.WIDTH // (2 * self.board.size) - 10,
                        self.board.size,
                    )
                if symbol == const.PLAYER_1:
                    pygame.draw.line(
                        self.screen,
                        const.BLUE,
                        (
                            col * const.WIDTH // self.board.size
                            + const.WIDTH // (2 * self.board.size)
                            - const.WIDTH // (2 * self.board.size)
                            + 10,
                            row * const.HEIGHT // self.board.size
                            + const.HEIGHT // (2 * self.board.size)
                            - const.HEIGHT // (2 * self.board.size)
                            + 10,
                        ),
                        (
                            col * const.WIDTH // self.board.size
                            + const.WIDTH // (2 * self.board.size)
                            + const.WIDTH // (2 * self.board.size)
                            - 10,
                            row * const.HEIGHT // self.board.size
                            + const.HEIGHT // (2 * self.board.size)
                            + const.HEIGHT // (2 * self.board.size)
                            - 10,
                        ),
                        self.board.size,
                    )
                    pygame.draw.line(
                        self.screen,
                        const.BLUE,
                        (
                            col * const.WIDTH // self.board.size
                            + const.WIDTH // (2 * self.board.size)
                            + const.WIDTH // (2 * self.board.size)
                            - 10,
                            row * const.HEIGHT // self.board.size
                            + const.HEIGHT // (2 * self.board.size)
                            - const.HEIGHT // (2 * self.board.size)
                            + 10,
                        ),
                        (
                            col * const.WIDTH // self.board.size
                            + const.WIDTH // (2 * self.board.size)
                            - const.WIDTH // (2 * self.board.size)
                            + 10,
                            row * const.HEIGHT // self.board.size
                            + const.HEIGHT // (2 * self.board.size)
                            + const.HEIGHT // (2 * self.board.size)
                            - 10,
                        ),
                        self.board.size,
                    )

    def main_loop(self):
        while True:
            mouse = pygame.mouse.get_pos()

            if (
                self.board.turn != cfg.PLAYER
                and self.board.state() == const.NOT_FINISHED
            ):
                move = self.ai.get_move()
                self.board.move(*move)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and self.board.turn == cfg.PLAYER
                    and self.board.state() == const.NOT_FINISHED
                ):
                    x, y = mouse[0] // (const.WIDTH // self.board.size), mouse[1] // (
                        const.HEIGHT // self.board.size
                    )
                    self.board.move(y, x)

            self.draw_board()

            if self.board.state() == const.PLAYER_1_WON:
                self.draw_text(f"{const.PLAYER_1} WON!")
            elif self.board.state() == const.PLAYER_2_WON:
                self.draw_text(f"{const.PLAYER_2} WON!")
            elif self.board.state() == const.DRAW:
                self.draw_text("DRAW!")

            pygame.display.update()
