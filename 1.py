import pygame
import random

# Константы
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Цвета
COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
]

# Фигуры Тетриса
SHAPES = [
    [[1, 1, 1], [0, 1, 0]],
    [[0, 2, 2], [2, 2, 0]],
    [[3, 3, 0], [0, 3, 3]],
    [[4, 4, 4, 4]],
    [[5, 5], [5, 5]],
    [[6, 6, 0], [0, 6, 6]],
    [[0, 7, 7], [7, 7, 0]],
]

class Score:
    def __init__(self):
        self.score = 0

    def add_score(self, lines):
        if lines == 1:
            self.score += 40
        elif lines == 2:
            self.score += 100
        elif lines == 3:
            self.score += 300
        elif lines == 4:
            self.score += 1200

    def reset(self):
        self.score = 0

    def display(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(text, (10, 10))

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = Score()

    def new_piece(self):
        return random.choice(SHAPES)

    def draw_board(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = COLORS[self.board[y][x]]
                pygame.draw.rect(self.screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    def draw_piece(self, piece, offset):
        off_x, off_y = offset
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, COLORS[cell], ((off_x + x) * GRID_SIZE, (off_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    def clear_lines(self):
        lines_cleared = 0
        for i in range(GRID_HEIGHT):
            if 0 not in self.board[i]:
                del self.board[i]
                self.board.insert(0, [0 for _ in range(GRID_WIDTH)])
                lines_cleared += 1
        self.score.add_score(lines_cleared)

    def run(self):
        while not self.game_over:
            self.screen.fill((0, 0, 0))
            self.draw_board()
            self.draw_piece(self.current_piece, (5, 5))  # Примерные координаты
            self.score.display(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

            self.clear_lines()

            pygame.display.flip()
            self.clock.tick(30)

if __name__ == "__main__":
    game = Tetris()
    game.run()